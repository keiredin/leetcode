class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if len(s) <= 1: return 1 
        graph = defaultdict(list)
        
        for i in range(len(s)):
            graph[parent[i]].append(i)
        
        maxLen = 0
        def dfs(i):
            nonlocal maxLen
            if i not in graph:
                return 1
            
            answ = [0,0]
            for child in graph[i]:
                res = dfs(child)
                if s[i] != s[child]:
                    answ.append(res)
                    
            answ.sort()
            maxLen = max(maxLen, answ[-1] + answ[-2] + 1)
            
            return answ[-1] + 1
        
        dfs(0)
        return maxLen
            
                