class Solution:
    def shortestAlternatingPaths(self, N, red_edges, blue_edges) -> List[int]:
        adj_list = defaultdict(list)
        for u,v in red_edges: adj_list[u].append((v, 0)) # 0 - red, 1 - blue
        for u,v in blue_edges: adj_list[u].append((v, 1))
            
        queue = deque([(0,0),(0,1)]) # (node, last_color), start with red and blue pills
        
        dist = [float(inf)] * N
        visited = set()
        level = 0
        while queue:
            for _ in range(len(queue)):
                node, last_color = queue.popleft()
                dist[node] = min(dist[node], level)

                for nei,edge_color in adj_list[node]:
                    if last_color != edge_color and (nei, edge_color) not in visited:
                        visited.add((nei, edge_color))
                        queue.append((nei, edge_color))
            level += 1
        
        return [d if d != float(inf) else -1 for d in dist]