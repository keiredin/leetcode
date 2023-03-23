class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
       
        
            
        visited = set()
        def dfs(i):
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)
            return 
        
        numberOfConnectedComponents = 0
        for i in range(n):
            if i not in visited:
                numberOfConnectedComponents += 1
                dfs(i)
                
        return numberOfConnectedComponents - 1
            
        
        