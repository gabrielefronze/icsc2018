from __future__ import division, print_function
import sys

#TODO fix this method
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    print(fib(int(sys.argv[1])))

if __name__ == '__main__':
    main()

