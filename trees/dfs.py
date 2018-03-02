from __future__ import division, print_function
from tree import TreeWalker

class Stack:
    def __init__(self):
        self.__list = list()
    def empty(self):
        pass #TODO fill in!
    def push(self, x):
        pass #TODO fill in!
    def pop(self):
        pass #TODO fill in!

def dfs(tree):
    discovered = list()
    s = Stack()
    #TODO DFS here
    return discovered

if __name__ == '__main__':
    TreeWalker(dfs).run()

