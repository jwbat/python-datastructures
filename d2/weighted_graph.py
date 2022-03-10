'''
Weighted UGraph.
  • Dijkstra's shortest path algorithm
  • Prim's algorithm for Minimum Spanning Trees
'''
from heapq import heapify, heappush, heappop


class WeightedGraph:
    def __init__(self):
        self.nodes = {}  # {node.label: node obj}

    def add_node(self, label):
        self.nodes[label] = _Node(label)

    def add_edge(self, fr, to, weight):
        from_node = self.nodes.get(fr)
        to_node = self.nodes.get(to)
        if not from_node or not to_node:
            raise KeyError()
        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)

    def contains_node(self, label):
        return label in self.nodes.keys()

    def has_cycle(self):
        visited, all_labels = set(), list(self.nodes.keys())
        def _has_cycle(label, previous, visited):
            visited.add(label)
            for edge in self.nodes.get(label).get_edges():
                to = edge.to.label
                if previous == to:
                    continue
                neighbor = to
                if neighbor in visited or \
                   _has_cycle(neighbor, label, visited):
                    return True

        for label in all_labels:
            if label not in visited and \
               _has_cycle(label, None, visited):
                    return True
        return False

    def get_shortest_path(self, fr, to):
        table = self.get_shortest_distance(fr, to)
        def _get_path(fr, to):
            if to == fr:
                return [to]
            return _get_path(fr, table.prevnodes.get(to)) + [to]
        return _get_path(fr, to)

    def create_queue_member(self, node, priority):
        f = lambda node, priority: _NodeEntry(node, priority)
        g = lambda ne: (ne.priority, ne.node)
        h = lambda node, priority: g(f(node, priority))
        # h ~~>  heap-friendly
        return h(node, priority)

    def get_minimum_spanning_tree(self):
        startnode = next(iter(self.nodes.values()))

        h = lambda edge: (edge.weight, edge)
        pq =  [h(edge) for edge in startnode.get_edges()]
        heapify(pq)                      # priority queue

        mst = WeightedGraph()
        mst.add_node(startnode.label)

        while len(mst.nodes) < len(self.nodes):
            min_edge  = heappop(pq)[1]
            nextnode = min_edge.to

            if mst.contains_node(nextnode.label):
                continue

            mst.add_node(nextnode.label)
            mst.add_edge(min_edge.fr.label, min_edge.to.label, min_edge.weight)

            for edge in nextnode.get_edges():
                if not mst.contains_node(edge.to.label):
                    heappush(pq, h(edge))

        return mst

    def get_shortest_distance(self, fr, to):
        from_node = self.nodes.get(fr)
        visited = set() # set of node objects

        h = self.create_queue_member
        queue = [h(from_node, 0)]
        table = _Table(list(self.nodes.keys()), startnode=fr)

        while queue:
            current = heappop(queue)[1]
            visited.add(current)

            for edge in current.get_edges():
                if edge.to in visited:
                    continue
                new_distance = table.distances.get(current.label) + edge.weight
                prevnode = current.label
                if new_distance < table.distances.get(to):
                    table.update(edge.to.label, new_distance, prevnode)
                    node, priority = edge.to, new_distance
                    heappush(queue, h(node, priority))

        return table

    def print(self):
        print()
        all_edges = set()
        for node in self.nodes.values():
            edges = node.get_edges()
            for edge in edges:
                print(f'\t{edge}')
        print()


class _Table:
    def __init__(self, vertices, startnode):
        self.vertices = vertices  #  lst of labels (strings)
        self.distances = self.initialize_distances(startnode) # {label: int}
        self.prevnodes = {vertex: '' for vertex in self.vertices} # {label: label}

    def get(self):
        return self.distances, self.prevnodes

    def update(self, vertex, distance, prevnode):
        self.distances[vertex] = distance
        self.prevnodes[vertex] = prevnode

    def initialize_distances(self, startnode): # startnode is a str
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[startnode] = 0
        return distances

    def show(self):
        distances, prevnodes = self.distances, self.prevnodes

        print('\n\n', '~' * 25, 'Table', '~' * 25, '\n')
        print('Node'.rjust(10), 'Distance'.rjust(10), 'Previous'.rjust(10))

        for vertex in self.vertices:
            node_label = f'{vertex}'.rjust(10)
            distance = f'{distances[vertex]}'.rjust(10)
            previous = f'{prevnodes[vertex]}'.rjust(10)
            print(node_label, distance, previous)


class _NodeEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def update(self, distance):
        self.priority = distance

    def __repr__(self):
        return f'({self.priority}, {self.node})'


class _Node:
    def __init__(self, label):
        self.label = label
        self.edges = [] # [edge objects]

    def add_edge(self, to, weight):
        self.edges.append(_Edge(self, to, weight))

    def get_edges(self):
        return self.edges

    def __repr__(self):
        return f'{self.label}'


class _Edge:
    def __init__(self, fr, to, weight):
        self.fr = fr # node obj
        self.to = to # node obj
        self.weight = weight

    def get_edge_set(self):
        return set(self.fr, self.to)

    def __repr__(self):
        return f'{self.fr} --{self.weight}--> {self.to}'


def main():
    def build():
        graph = WeightedGraph()
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')
        graph.add_node('E')
        graph.add_edge('A', 'B', 6)
        graph.add_edge('A', 'D', 1)
        graph.add_edge('D', 'E', 1)
        graph.add_edge('D', 'B', 2)
        graph.add_edge('E', 'B', 2)
        graph.add_edge('E', 'C', 5)
        graph.add_edge('B', 'C', 5)
        print('graph.print(): ')
        graph.print()
        print('-' * 70)

        fr, to = 'A', 'C'
        path = graph.get_shortest_path(fr, to)
        print(f'\n\t shortest path from {fr} to {to}: ', path)

    def test_has_cycle():
        graph = WeightedGraph()
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')

        graph.add_edge('A', 'B', 1)
        graph.add_edge('B', 'C', 1)
        graph.add_edge('C', 'D', 1)
        graph.print()
        print('\n\t has cycle: ', graph.has_cycle())

    def test_minimum_spanning_tree():
        graph = WeightedGraph()
        graph.add_node('A')
        graph.add_node('B')
        graph.add_node('C')
        graph.add_node('D')

        graph.add_edge('A', 'B', 3)
        graph.add_edge('A', 'C', 1)
        graph.add_edge('B', 'C', 2)
        graph.add_edge('B', 'D', 4)
        graph.add_edge('C', 'D', 5)

        print('\n\tMinimum Spanning Tree: ', )
        mst = graph.get_minimum_spanning_tree()
        mst.print()

    test_minimum_spanning_tree()
    #test_has_cycle()
    #build()
    print()

main()
