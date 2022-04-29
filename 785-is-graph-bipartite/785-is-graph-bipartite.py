class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # white -> uncoloured
        table = defaultdict(lambda: "white")
        q = deque([0])
		# just in case graph is disconnected
        for node in range(len(graph)):
            if node not in table:
                table[node] = "red"
                q.append(node)
                while len(q):
                    curr = q.popleft()
                    for adj_node in graph[curr]:
                        if table[adj_node] == table[curr]:
                            return False
                        if table[adj_node] == "white":
                            table[adj_node] = "blue" if table[curr] == "red" else "red"
                            q.append(adj_node)
        return True
        