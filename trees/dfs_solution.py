from __future__ import division, print_function
from tree import TreeWalker

class Stack:
    def __init__(self):
        self.__list = list()
    def empty(self):
        return len(self.__list) == 0
    def push(self, x):
        self.__list.append(x)
    def pop(self):
        return self.__list.pop()

def dfs(tree):
    discovered = list()
    s = Stack()
    s.push(tree.head)
    while not s.empty():
        n = s.pop()
        discovered.append(n)
        for child in reversed(n.children):
            s.push(child)
    return discovered

if __name__ == '__main__':
    TreeWalker(dfs).run()

