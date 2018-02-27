from __future__ import division, print_function
import sys

cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    elif n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

def main():
    print(fib(int(sys.argv[1])))

if __name__ == '__main__':
    main()

