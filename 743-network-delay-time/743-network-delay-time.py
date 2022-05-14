class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # establish graph and data structures
        total_time_to_reach_node = {i: float('inf') for i in range(1, n+1)}
        graph = defaultdict(list)
        for src, target, time in times:
            if src in graph: 
                graph[src].append((target, time))
            else:
                graph[src] = [(target, time)]

        queue = [(k, 0)]

        # bfs until no new updates are made
        while queue:
            src, total_time = queue.pop(0)
            if total_time < total_time_to_reach_node[src]:
                total_time_to_reach_node[src] = total_time
                for target, time in graph[src]:
                    queue.append((target, total_time + time))    

        # if possible, return the total time to traverse network
        time_to_traverse_network = max(total_time_to_reach_node.values())
        if time_to_traverse_network < float('inf'):
            return time_to_traverse_network
        else:
            return -1