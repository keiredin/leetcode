class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        
        adj_list = defaultdict(list)
        
        for x,y,w in times:
            adj_list[x].append((w, y))
        
        visited=set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited)==n:
                return travel_time
            
            for time, adjacent_node in adj_list[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time+time, adjacent_node))
                
        return -1


# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         # establish graph and data structures
#         total_time_to_reach_node = {i: float('inf') for i in range(1, n+1)}
#         graph = defaultdict(list)
#         for src, target, time in times:
#             if src in graph: 
#                 graph[src].append((target, time))
#             else:
#                 graph[src] = [(target, time)]

#         queue = [(k, 0)]

#         # bfs until no new updates are made
#         while queue:
#             src, total_time = queue.pop(0)
#             if total_time < total_time_to_reach_node[src]:
#                 total_time_to_reach_node[src] = total_time
#                 for target, time in graph[src]:
#                     queue.append((target, total_time + time))    

#         # if possible, return the total time to traverse network
#         time_to_traverse_network = max(total_time_to_reach_node.values())
#         if time_to_traverse_network < float('inf'):
#             return time_to_traverse_network
#         else:
#             return -1