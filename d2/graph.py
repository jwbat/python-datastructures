'''
Directed Graph.
'''
from collections import deque

class Graph:
    def __init__(self):
        self.nodes = {}     # {node.label: Node obj}
        self.adjacency = {} # {node.label : [node list]}

    def add_node(self, label):
        node = _Node(label)
        self.nodes[label] = node
        self.adjacency[label] = []

    def remove_node(self, label):
        node = self.nodes.get(label)
        if not node: return

        for n in self.adjacency:
            try:
                self.adjacency.get(n).remove(node)
            except:
                pass
        del self.adjacency[label]
        del self.nodes[label]

    def add_edge(self, fr, to):
        from_node = self.nodes.get(fr)
        to_node = self.nodes.get(to)
        if not from_node or not to_node:
            raise KeyError()
        self.adjacency[fr].append(to_node)

    def remove_edge(self, fr, to):
        from_node = self.nodes.get(fr)
        to_node = self.nodes.get(to)
        if not from_node or not to_node:
            return
        try:
            self.adjacency.get(fr).remove(to_node)
        except:
            pass

    # recursive version
    def traverse_depth_first(self, label):
        if label not in self.nodes:
            return

        def _traverse(node, visited):
            for neighbor in self.adjacency.get(node.label):
                if neighbor.label not in set(visited):
                    visited.append(neighbor.label)
                    _traverse(neighbor, visited)
            return visited
        return _traverse(_Node(label), [label])


    def has_cycle(self):
        allnodes, visiting, visited  = set(self.nodes.keys()), set(), set()

        def _has_cycle(label, allnodes, visiting, visited):
            if label in allnodes:
                allnodes.remove(label)
            visiting.add(label)

            for child in self.adjacency.get(label):
                if child in visited:
                    continue
                if child.label in visiting:
                    return True

                if _has_cycle(child.label, allnodes, visiting, visited):
                    return True

            visiting.remove(label)
            visited.add(label)
            return False

        while allnodes:
            if _has_cycle(allnodes.pop(), allnodes, visiting, visited):
                return True
        return False


    def topological_sort(self):
        stack = deque()
        visited = set()

        def _sort(label):
            visited.add(label)
            for neighbor in self.adjacency.get(label):
                if neighbor.label not in visited:
                    _sort(neighbor.label)
            stack.append(label)

        for label in list(self.nodes.keys()):
            if label not in visited:
                _sort(label)

        return [stack.pop() for _ in range(len(stack))]


    # iterative version
    def traverse_depth_first2(self, label):
        if label not in self.nodes:
            return

        stack = deque()
        stack.append(label)

        visited = set()
        while len(stack):
            current = stack.pop()
            if current in visited:
                continue
            print('\t', current)
            visited.add(current)

            for neighbor in self.adjacency.get(current):
                if neighbor.label not in visited:
                    stack.append(neighbor.label)

    def traverse_breadth_first(self, label):
        if label not in self.nodes:
            return

        queue = deque()
        queue.append(label)

        visited = set()
        while len(queue):
            current = queue.popleft()
            if current in visited:
                continue
            print('\t', current)
            visited.add(current)

            for neighbor in self.adjacency.get(current):
                if neighbor.label not in visited:
                    queue.append(neighbor.label)


    def print(self):
        print()
        for source in self.adjacency:
            targets = self.adjacency.get(source)
            if targets:
                print(f'\t{source} is connected to {targets}')
        print()


class _Node:
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return f'{self.label}'


def main():
    def build():
        graph = Graph()
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('D', 'C')
        graph.print()
        return graph

    def traverse(graph):
        lst = graph.traverse_depth_first('A')
        print('\n\t visited: ', lst, '\n')

        print('\n\t traverse depth first: ')
        graph.traverse_depth_first2('A')

        print('\n\t traverse breadth first: ')
        graph.traverse_breadth_first('A')

    def test_topological_sort():
        graph = Graph()
        graph.add_node('W')
        graph.add_node('X')
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('P')
        graph.add_edge('W', 'X')
        graph.add_edge('X', 'A')
        graph.add_edge('X', 'B')
        graph.add_edge('A', 'P')
        graph.add_edge('B', 'P')

        lst = graph.topological_sort()
        print('\n\t', lst, '\n')

    #test_topological_sort()

    def test_has_cycle():
        def add_nodes():
            graph = Graph()
            graph.add_node('A')
            graph.add_node('B')
            graph.add_node('C')
            graph.add_node('D')
            return graph

        def make_acyclic_graph():
            graph = add_nodes()
            graph.add_edge('A', 'B')
            graph.add_edge('B', 'C')
            graph.add_edge('A', 'C')
            graph.add_edge('D', 'A')
            return graph

        def make_cyclic_graph():
            graph = add_nodes()
            graph.add_edge('A', 'B')
            graph.add_edge('B', 'C')
            graph.add_edge('C', 'A')
            graph.add_edge('D', 'A')
            return graph

        acyclic_graph = make_acyclic_graph()
        print('\n\t The acyclic graph has a cycle: ', acyclic_graph.has_cycle(), '\n')

        cyclic_graph = make_cyclic_graph()
        print('\n\t The cyclic graph has a cycle: ', cyclic_graph.has_cycle(),'\n')

    test_has_cycle()

main()




