from __future__ import division, print_function
import math
import sys
INFINITY = sys.maxsize

class Graph:
    """
    A Graph is just a container for nodes and edges, with some utility
    built-in.
    """
    def __init__(self, nodes, edges):
        self.__nodes = frozenset(nodes)
        self.__edges = frozenset(edges)
    @property
    def nodes(self): return self.__nodes
    @property
    def edges(self): return self.__edges

    def get_edges(self, node):
        if hasattr(node, '_edges'):
            # Use the cached value
            return node._edges

        my_edges = []
        for edge in self.edges:
            if edge.fr == node:
                my_edges.append(edge)
        node._edges = frozenset(my_edges)
        return node._edges

class Node:
    """
    A Node has an (optional) name. Other than that it only functions as an
    identifier.
    """
    def __init__(self, name = ''):
        assert(isinstance(name, str))
        self.__name = name
    @property
    def name(self): return self.__name
    def __str__(self): return self.name
    def __repr__(self): return self.name

class Edge:
    """
    The Edge is where the magic lives: it connects node 'fr' (from) to 'to',
    with a certain weight.
    """
    def __init__(self, fr, to, weight):
        assert(isinstance(fr, Node) and isinstance(to, Node) and isinstance(weight, (int, float)))
        self.__fr = fr
        self.__to = to
        self.__weight = weight
    @property
    def fr(self): return self.__fr
    @property
    def to(self): return self.__to
    @property
    def weight(self): return self.__weight

def dijkstra(graph, start_node):
    estimated_distances = {x: 0 if x == start_node else INFINITY for x in graph.nodes}
    visited_nodes = set()
    current_node = start_node
    # TODO implement Dijkstra's algorithm

    return estimated_distances

def main():
    """
    A trivial example with three nodes and two edges.
    """
    def testcase_trivial():
        nodes = [Node() for _ in range(3)]
        graph = Graph(nodes = nodes,\
                edges = [Edge(nodes[0], nodes[1], 2), Edge(nodes[0], nodes[2], 3)])
        solution = {nodes[0]: 0, nodes[1]: 2, nodes[2]: 3}
        return (graph, nodes[0], solution)

    """
    The example from the slides!
    """
    def testcase_lecture():
        nodes = [Node('A'), Node(), Node('B'), Node(), Node()]
        graph = Graph(nodes = nodes, edges = [\
                Edge(nodes[0], nodes[1], 10),\
                Edge(nodes[0], nodes[3],  5),\
                Edge(nodes[1], nodes[2],  1),\
                Edge(nodes[1], nodes[3],  3),\
                Edge(nodes[2], nodes[4],  6),\
                Edge(nodes[3], nodes[1],  2),\
                Edge(nodes[3], nodes[2],  9),\
                Edge(nodes[3], nodes[4],  2),\
                Edge(nodes[4], nodes[0],  7),\
                Edge(nodes[4], nodes[3],  4),\
                ])
        solution = {nodes[0]: 0, nodes[1]: 7, nodes[2]: 8, nodes[3]: 5, nodes[4]: 7}
        return (graph, nodes[0], solution)

    """
    This is the roadnet of Rome, Italy, in 1999 (from
    http://www.dis.uniroma1.it/challenge9/data/rome/rome99.gr). This is a
    pretty large network, with over 3000 nodes and almost 9000 edges.
    """
    def testcase_roadnet_Rome():
        edges = []
        with open('../data/rome99.gr') as f:
            for line in f.readlines():
                parts = line.split(' ')
                if parts[0] == 'c': continue # comment
                if parts[0] == 'p': # problem (specification)
                    nodes = [Node(str(i)) for i in range(int(parts[2]))]
                elif parts[0] == 'a': # arc (edge)
                    # The file specification is 'to' 'from' 'weight'
                    edges.append(Edge(nodes[int(parts[2]) - 1], nodes[int(parts[1]) - 1], int(parts[3])))
        from rome_solution import solution
        return (Graph(nodes, edges), nodes[1479], {nodes[key]: value for key, value in solution.items()})

    """
    This test case is a graph of all the road networks in California (from
    http://snap.stanford.edu/data/roadNet-CA.html). This graph has close to 2
    million nodes and about 5.5 million edges. This is the ultimate test!
    """
    def testcase_roadnet_CA():
        edges_plain = []
        n_nodes = 0
        with open('../data/roadNet-CA.txt') as f:
            for line in f.readlines():
                if line[0] == '#': continue
                parts = line.split('\t')
                fr = int(parts[0].strip())
                to = int(parts[1].strip())
                edges_plain.append((fr, to))
                n_nodes = max(n_nodes, fr, to)
        nodes = [Node() for _ in range(n_nodes)]
        graph = Graph(nodes = nodes,\
                edges = [Edge(nodes[fr - 1], nodes[to - 1], 1) for (fr, to) in edges_plain])
        return (graph, None)

    def run_testcase(name, graph, start_node, solution):
        result = dijkstra(graph, start_node)
        success = (result == solution)

        # The rest of this method is a lot of code to pretty-print the result...
        result = {node: 'INFINITY' if value == INFINITY else str(value) for node, value in result.items()}
        for node in set(solution.keys()) - set(result.keys()):
            result[node] = 'MISSING'
        solution = {node: 'INFINITY' if value == INFINITY else str(value) for node, value in solution.items()}

        format_string = 'Node '

        name_lengths = [len(str(x)) for x in solution.keys()]
        shortest_name = min(name_lengths)
        longest_name = max(name_lengths)
        if shortest_name == 0: # Not all nodes have a name
            longest_index = int(math.ceil(math.log(len(solution), 10)))
            format_string += '{index:>' + str(longest_index) + '}'
            if longest_name != 0:
                # ... but at least one node does have a name!
                format_string += ' ({name:>' + str(longest_name) + '})'
        else:
            # All nodes have names, use them!
            format_string += '{name:>' + str(longest_name) + '}'

        longest_result = max(map(len, result.values()))
        format_string += ': {result:>' + str(longest_result) + '}'

        longest_solution = max(map(len, solution.values()))
        format_string_fail = format_string + ', expected {solution:>' + str(longest_solution) + '}'

        print('{}: {}'.format(name, 'success' if success else 'failed'))
        # Sort, but only if we print everything by name
        sorted_solution = solution if shortest_name == 0 else sorted(solution.keys(), key = lambda x: int(str(x)) if str(x).isdigit() else str(x))
        for i, node in zip(range(len(sorted_solution)), sorted_solution):
            my_format = format_string if result[node] == solution[node] else format_string_fail
            print(my_format.format(index=i, name=str(node), result=result.get(node, 'MISSING'), solution=solution[node]))
        if len(solution) > 10:
            print('{}: {}'.format(name, 'success' if success else 'failed'))
        print()

    run_testcase('Trivial graph', *testcase_trivial())
    run_testcase('Lecture example', *testcase_lecture())
    #run_testcase('Rome roads', *testcase_roadnet_Rome())
    #run_testcase('California roads', *testcase_roadnet_CA())

if __name__ == '__main__':
    main()

