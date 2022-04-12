class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_len = len(graph)
        safeNode = {}


        def dfs(node):
            if node in safeNode:
                return safeNode[node]
            safeNode[node] = False
            for neighbour in graph[node]:
                if dfs(neighbour) == False :
                    return False
            safeNode[node] = True
            return True
        
        answ = []
        for node in range(graph_len):
            if dfs(node) == True:
                answ.append(node)
                
        return answ













# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         graph_len = len(graph)
#         terminal = {i for i in range(graph_len) if graph[i] == []}
#         safeNode = []
#         visited = set()
        
        
        
#         def dfs(node):
#             visited.add(node)
#             dfs_stack.add(node)
            
#             for neighbour in graph[node]:
#                 if neighbour not in visited:
#                     if dfs(neighbour) == False:
#                         return False
#                 else:
#                     return False
                
#             safeNode.append(node)
#             return True
        
#         for node in range(graph_len):
#             visited = set()

               
#         return safeNode
                
                    
        