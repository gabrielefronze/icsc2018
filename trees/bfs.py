from __future__ import division, print_function
from tree import TreeWalker

class Queue:
    def __init__(self):
        self.__list = list()
    def empty(self):
        pass #TODO fill in!
    def enqueue(self, x):
        pass #TODO fill in!
    def dequeue(self):
        pass #TODO fill in!

def bfs(tree):
    discovered = list()
    q = Queue()
    #TODO BFS here
    return discovered

if __name__ == '__main__':
    TreeWalker(bfs).run()

