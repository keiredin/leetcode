class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        def dfs(node):
            
            answ = []
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    answ.append(dfs(nei))
            if not answ:
                return hasApple[node]
            
            cost = 0
            for res in answ:
                cost += res
            # print(cost, node)
            
            if cost:
                return cost + 1
            else:
                return hasApple[node]
            
        
        visited = set()
        visited.add(0)
        answ = (dfs(0) - 1) * 2
        
        return answ if answ > 0 else 0
        
                
        