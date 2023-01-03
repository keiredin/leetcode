class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            a,b = edges[i]
            if vals[b] > 0:
                graph[a].append(vals[b])
            if vals[a] > 0:
                graph[b].append(vals[a])
                
        
        for val in graph.keys():
            graph[val].sort(reverse=True)
        
        maxResult = -10 ** 4
        for i in range(len(vals)):
            maxResult = max(maxResult, vals[i] + sum(graph[i][:k]))
            
        return maxResult
    
#         def dfs(node,parent):
#             nonlocal maxAns
            
#             neighbors = [parent]
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     neighbors.append(dfs(neighbor, vals[node]))
            
#             t = k
#             neighbors.sort(reverse=True)
#             totalSum = 0
#             print(neighbors)
#             for i in range(len(neighbors)):
#                 if t > 0 and neighbors[i] > 0:
#                     totalSum += neighbors[i]
#                     t -= 1
#                 else:
#                     break
           
#             totalSum += vals[node]
#             maxAns = max(maxAns, totalSum)
            
#             return vals[node]
        
#         visited = set()
#         for i in range(len(vals)):
#             dfs(i,0)
#         return maxAns
    
                    
            
            
            

        