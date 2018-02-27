from __future__ import division, print_function
import sys

def fib(n):
    previous = 0
    previous_previous = 0
    for i in range(n):
        if i <= 1:
            this_one = 1
        else:
            this_one = previous + previous_previous
        previous_previous = previous
        previous = this_one
    return this_one

def main():
    print(fib(int(sys.argv[1])))

if __name__ == '__main__':
    main()

