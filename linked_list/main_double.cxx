#include <ctime>
#include <functional>
#include <iostream>
#include <vector>

#include "linked_list_double.h"

using std::cout;
using std::endl;

void time(std::function<void()> function, const char* label)
{
    const std::clock_t start = std::clock();
    function();
    const std::clock_t end = std::clock();
    cout << "Time (ms) spent on " << label << ": " << (end - start) * 1000. / CLOCKS_PER_SEC << endl;
}

template <class C>
void print_all(const C& collection)
{
    for (const auto& x : collection)
    {
        cout << x << endl;
    }
}

int main(int argc, char** argv)
{
    const std::uint_least32_t N_ITEMS =
        argc >= 2 ? atoi(argv[1]) : 10;

    linked_list<int> l;
    std::vector<int> v;

    time([&l, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                l.push_front(i);
            }
        }, "linked list push_front");

    // print_all(l);

    time([&l, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                l.push_back(i);
            }
        }, "linked list push_back");

    // Determining the size many times - should be fast!
    time([&l, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                l.size();
            }
        }, "linked list size");

    time([&l, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                l.pop_front();
            }
        }, "linked list pop_front");

    time([&l, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                l.pop_back();
            }
        }, "linked list pop_back");

    time([&v, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                v.push_back(i);
            }
        }, "vector push_back");

    time([&v, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                v.size();
            }
        }, "vector size");

    time([&v, &N_ITEMS] {
            for (std::remove_cv<decltype(N_ITEMS)>::type i = 0; i < N_ITEMS; ++i)
            {
                v.pop_back();
            }
        }, "vector pop_back");

}

