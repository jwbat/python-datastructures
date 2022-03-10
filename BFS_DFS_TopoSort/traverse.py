from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.adjacency = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency[u].append(v)

    def print_graph(self):
        for u in self.adjacency:
            print(u, ": ", self.adjacency[u])

    def DFS(self, u, visited):
        visited.add(u)
        # print nodes being visited
        print(u, end='  ')
        if u in self.adjacency:
            for neighbor in self.adjacency[u]:
                if neighbor not in visited:
                    self.DFS(neighbor, visited)

    def DFS2(self, u):
        visited = set()
        stack = [u]
        while stack:
            u = stack.pop()
            print(u, end= '  ')
            visited.add(u)
            if u in self.adjacency:
                for neighbor in self.adjacency[u]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    def BFS(self, u):
        visited = set()
        queue = deque([u])
        while queue:
            u = queue.popleft()
            print(u, end= '  ')
            visited.add(u)
            if u in self.adjacency:
                for neighbor in self.adjacency[u]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def topo_sort(self, u, visited, visiting, stack):
        visited.add(u)
        visiting.add(u)
        if u in self.adjacency:
            for neighbor in self.adjacency[u]:
                if neighbor in visiting:
                    raise Exception('cycle!')
                if neighbor not in visited:
                    self.topo_sort(neighbor, visited, visiting, stack)
        stack.append(u)
        visiting.remove(u)




#       -- 0 --
#       |     |
#       1     2
#       |     |
#       3     4
#
#

# 0 -> 1, 2 
# 1 -> 3
# 2 -> 4
g = Graph()
edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
for edge in edges:
    g.add_edge(*edge)

print('================================\n')
g.print_graph()
print('\n================================')

print('DFS recursive: ', end='  ')
g.DFS(0, set())  # 0 1 3 2 4

print('\n================================')

print('DFS iterative: ', end='  ')
g.DFS2(0)  # 0 2 4 1 3

print('\n================================')

print('BFS iterative: ', end='  ')
g.BFS(0) # 0 1 2 3 4
print("\n")

print('\n================================')

stack = []
g.topo_sort(0, set(), set(), stack)  # visiting set catches cycles
#try:
#    g.topo_sort(0, set(), set(), stack)  # visiting set catches cycles
#except:
#    print(None)

print("\n") # 3 1 4 2 0  (several valid sorts)
print(stack) # -> 3 depends on 1, 4 depends on 2, etc.
