#ifndef LINKED_LIST_H
#define LINKED_LIST_H

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
            : item{t}, next{}
        {
        }

        T item;
        std::unique_ptr<linked_list_node<T>> next;
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
            if (!head)
            {
                head = make_unique<node>(node(t));
                return;
            }

            auto old_head = std::move(head);
            head = make_unique<node>(node(t));
            head->next = std::move(old_head);
        }

        void push_back(const_reference t)
        {
            if (!head)
            {
                head = make_unique<node>(node(t));
                return;
            }

            node* current = &(*head);
            while (current != nullptr)
            {
                if (!current->next)
                {
                    current->next = make_unique<node>(node(t));
                    return;
                }
                current = &(*current->next);
            }
        }

        void pop_front()
        {
            if (!head->next)
            {
                head = nullptr;
                return;
            }

            head = std::move(head->next);
        }

        void pop_back()
        {
            if (!head->next)
            {
                head = nullptr;
                return;
            }

            node* current = &(*head);
            while (current != nullptr)
            {
                // check the next next node, if it's null, this is the second-to-last node
                if (!current->next->next)
                {
                    current->next = nullptr;
                    return;
                }
                current = &(*current->next);
            }
        }

        bool empty() const
        {
            return !head;
        }

        size_type size() const
        {
            if (!head)
            {
                return 0;
            }

            size_type n = 0;
            node* current = &(*head);
            while (current->next)
            {
                current = &(*current->next);
                ++n;
            }
            return n;
        }

        reference front() const
        {
            return head->item;
        }
        reference back()
        {
            node* current = &(*head);
            while (current->next)
            {
                current = &(*current->next);
            }
            return current->item;
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
        std::unique_ptr<node> head;
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

