from __future__ import division, print_function

class Tree:
    def __init__(self, head):
        assert(isinstance(head, Node))
        self.__head = head
    @property
    def head(self): return self.__head

    def __str__(self): return str(self.__head)

class Node:
    def __init__(self, value, childL = None, childR = None):
        assert(childL is None or isinstance(childL, Node))
        assert(childR is None or isinstance(childR, Node))
        self.__value = value
        self.__childL = childL
        self.__childR = childR

    @property
    def value(self): return self.__value
    @property
    def childL(self): return self.__childL
    @property
    def childR(self): return self.__childR
    @property
    def children(self): return list(filter(lambda c: c is not None, [self.childL, self.childR]))

    def __repr__(self): return str(self.value)

    def __str__(self, level = 1, lines = set()):
        ret = ''
        for l in range(level - 1):
            if l in lines:
                ret += '|   '
            else:
                ret += '    '
        ret += '+---' + str(self.value) + '\n'

        children = self.children
        for child in children:
            my_lines = set(lines)
            if not child == children[-1]:
                my_lines.add(level)
            ret += child.__str__(level + 1, my_lines)
        return ret

class TreeWalker:
    def __init__(self, algorithm):
        assert(callable(algorithm))
        self.__algorithm = algorithm

    def run(self):
        examples = self.get_examples()
        for example in examples:
            result = self.__algorithm(example)
            print(example)
            print('Result:')
            print(result)
            print()

    @classmethod
    def get_examples(cls):
        example1 = Tree(Node(1, Node(2), Node(3)))
        # example 2 is the tree from the lectures
        example2 = Tree(Node(8,\
                Node(3, Node(1), Node(6,\
                    Node(4), Node(7))),\
                Node(10, None, Node(14,\
                    Node(13), None))))
        # a larger example
        example3 = Tree(Node(20,\
                Node(12, Node(0, Node(30),\
                    Node(29)), example2.head),\
                Node(21, Node(15), Node(42,\
                    Node(25), Node(19)))))
        return [example1, example2]
        #TODO replace the line above with this one to run the larger example3
        #return [example1, example2, example3]

