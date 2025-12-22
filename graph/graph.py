from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}  # stores nodes and their connections

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        # Undirected graph → both ways connection
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def show(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return

        # Remove this vertex from all its neighbors
        for n in self.adj_list[vertex]:
            self.adj_list[n] = [
                v for v in self.adj_list[n] if v != vertex
            ]

        # Finally, delete the vertex itself
        del self.adj_list[vertex]

    # -----------------
    # BFS Traversal
    # -----------------
    def bfs(self, val):
        visited = set()
        result = []
        visited.add(val)
        queue = deque([val])
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for i in self.adj_list[vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return result

    # -----------------
    # DFS Traversal (iterative)
    # -----------------
    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        visited.add(start)

        while stack:
            vertex = stack.pop()
            result.append(vertex)
            for n in self.adj_list[vertex]:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
        return result


x = Graph()
x.add_edge("A", "B")
x.add_edge("A", "C")
x.add_edge("B", "D")
x.add_edge("E","F")

print("Before removal:")
x.show()

print("\nBFS from A:", x.bfs("A"))
print("DFS from A:", x.dfs("A"))

x.remove_vertex("A")

print("\nAfter removal of A:")
x.show()

print("\nBFS from B:", x.bfs("B"))
print("DFS from B:", x.dfs("B"))