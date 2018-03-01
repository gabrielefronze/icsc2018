#ifndef LINKED_LIST_SOLUTION_H
#define LINKED_LIST_SOLUTION_H

#include <memory>

#include "make_unique.h"

template<class T>
class linked_list;

template<class T>
class linked_list_iterator;

template<class T>
class linked_list_node
{
    friend class linked_list<T>;
    friend class linked_list_iterator<T>;

    private:
        explicit linked_list_node(const T& t)
            : item{t}, next{}, prev{nullptr}
        {
        }

        T item;
        std::unique_ptr<linked_list_node<T>> next;
        linked_list_node<T>* prev;
};

template<class T>
class linked_list
{
    using value_type = T;
    using reference = T&;
    using const_reference = const T&;
    using size_type = std::size_t;
    using node = linked_list_node<value_type>;
    using iterator = linked_list_iterator<value_type>;
    using const_iterator = linked_list_iterator<const value_type>;

    public:
        linked_list()
        {
        }

        reference operator[](size_type pos)
        {
            auto it = begin();
            while (pos > 0)
            {
                ++it;
                --pos;
            }
            return *it;
        }

        void push_front(const_reference t)
        {
            ++current_size;
            if (!head)
            {
                head = make_unique<node>(node(t));
                tail = &(*head);
                return;
            }

            auto old_head = std::move(head);
            head = make_unique<node>(node(t));
            old_head->prev = &(*head);
            head->next = std::move(old_head);
        }

        void push_back(const_reference t)
        {
            ++current_size;
            if (!head)
            {
                head = make_unique<node>(node(t));
                tail = &(*head);
                return;
            }

            const auto old_tail = tail;
            tail->next = make_unique<node>(node(t));
            tail = &(*tail->next);
            tail->prev = old_tail;
        }

        void pop_front()
        {
            if (!head->next)
            {
                head = nullptr;
                tail = nullptr;
                current_size = 0;
                return;
            }

            head = std::move(head->next);
            head->prev = nullptr;
            --current_size;
        }

        void pop_back()
        {
            if (!head->next)
            {
                head = nullptr;
                tail = nullptr;
                current_size = 0;
                return;
            }

            tail = tail->prev;
            tail->next = nullptr;
            --current_size;
        }

        bool empty() const
        {
            return !head;
        }

        size_type size() const
        {
            return current_size;
        }

        reference front() const
        {
            return head->item;
        }
        reference back()
        {
            return tail->item;
        }

        iterator begin() const
        {
            return iterator(&(*head));
        }
        iterator end() const
        {
            return iterator();
        }
        const_iterator cbegin() const
        {
            return begin();
        }
        const_iterator cend() const
        {
            return end();
        }

    private:
        size_type current_size;
        std::unique_ptr<node> head;
        node* tail;
};

template <class T>
class linked_list_iterator
{
    public:
        explicit linked_list_iterator(linked_list_node<T>* current = nullptr)
            : current(current)
        {
        }
        T& operator*() const
        {
            return current->item;
        }
        T& operator->() const
        {
            return *(*this);
        }
        linked_list_iterator<T> operator++()
        {
            current = current->next.get();
            return *this;
        }
        bool operator==(const linked_list_iterator<T>& other) const
        {
            return current == other.current;
        }
        bool operator!=(const linked_list_iterator<T>& other) const
        {
            return !(*this == other);
        }
        void operator++(int n)
        {
            while (n)
            {
                ++(*this);
                --n;
            }
            return *this;
        }
        operator linked_list_iterator<const T>() const
        {
            return linked_list_iterator<const T>(current);
        }
    private:
        linked_list_node<T>* current;
};

#endif

