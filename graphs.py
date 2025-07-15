class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        str_graphs = ""
        for key, value in self.adj_list.items():
            str_graphs += f"{key} -> {value}\n"
        return str_graphs

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node Already Exists!!")

    def add_edge(self, source_node, destination_node, weighted=None):
        if source_node not in self.adj_list:
            self.add_node(source_node)

        if destination_node not in self.adj_list:
            self.add_node(destination_node)

        # Unweighted edge
        if weighted is None:
            self.adj_list[source_node].add(destination_node)
            if not self.directed:
                self.adj_list[destination_node].add(source_node)
        else:
            self.adj_list[source_node].add((destination_node, weighted))
            if not self.directed:
                self.adj_list[destination_node].add((source_node, weighted))

    def get_neighbours(self, key_node):
        return self.adj_list.get(key_node, set())

    def bfs(self, start):
        """Breadth-First Search using a queue (FIFO)"""
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):  # for weighted edges
                        neighbour = neighbour[0]
                    if neighbour not in visited and neighbour not in queue:
                        queue.append(neighbour)
        return order

    def dfs(self, start):
        """Depth-First Search using a stack (LIFO)"""
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in sorted(neighbours, reverse=True):  # sort to keep order consistent
                    if isinstance(neighbour, tuple):  # for weighted edges
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def adj_matrix(self):
        # You can implement this later if needed
        pass

# Test
if __name__ == '__main__':
    graph_obj = Graphs(directed=False)
    graph_obj.add_edge("A", "B")
    graph_obj.add_edge("A", "C")
    graph_obj.add_edge("B", "D")
    graph_obj.add_edge("C", "D")
    graph_obj.add_edge("D", "E")

    print("Graph Structure:")
    print(graph_obj)

    print("BFS from A:", graph_obj.bfs("A"))
    print("DFS from A:", graph_obj.dfs("A"))
