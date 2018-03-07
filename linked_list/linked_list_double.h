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
            : item{t}, next{}, prev{}
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
            listsize=0;
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
            if (listsize==0)
            {
                head = make_unique<node>(node(t));
                tail = head.get();
                listsize=1;
                return;
            }

            auto old_head = std::move(head);
            head = make_unique<node>(node(t));
            head->prev = nullptr;
            head->next = std::move(old_head);
            head->prev = head.get();
            listsize++;
        }

        void push_back(const_reference t)
        {
            if (listsize==0)
            {
                head = make_unique<node>(node(t));
                tail = head.get();
                listsize=1;
                return;
            }

            tail->next = make_unique<node>(node(t));
            tail->next->prev = tail;
            tail = tail->next.get();
            listsize++;
        }

        void pop_front()
        {
            if (listsize==1)
            {
                head = nullptr;
                tail = nullptr;
                listsize=0;
                return;
            }

            head->next->prev = nullptr;
            head = std::move(head->next);
            listsize--;
        }

        void pop_back()
        {
            if (listsize==1)
            {
                head = nullptr;
                tail = nullptr;
                listsize=0;
                return;
            }

            tail = tail->prev;
            tail->next = nullptr;
            listsize--;
            return;          
        }

        bool empty() const
        {
            listsize=0;
            return !head;
        }

        size_type size() const
        {
            return listsize;
        }

        reference front() const
        {
            return head->item;
        }
        reference back() const
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
        std::unique_ptr<node> head;
        node* tail;
        size_type listsize;
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

