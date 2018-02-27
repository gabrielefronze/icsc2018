from __future__ import division, print_function
from tree import TreeWalker

class Queue:
    def __init__(self):
        self.__list = list()
    def empty(self):
        return len(self.__list) == 0
    def enqueue(self, x):
        return self.__list.append(x)
    def dequeue(self):
        return self.__list.pop(0)

def bfs(tree):
    discovered = list()
    q = Queue()
    q.enqueue(tree.head)
    while not q.empty():
        n = q.dequeue()
        discovered.append(n)
        for child in n.children:
            q.enqueue(child)
    return discovered

if __name__ == '__main__':
    TreeWalker(bfs).run()

