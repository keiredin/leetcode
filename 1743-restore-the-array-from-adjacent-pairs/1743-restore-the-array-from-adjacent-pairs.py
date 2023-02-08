class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            
        
        def dfs(curNum, res):
            res.append(curNum)
            for nei in graph[curNum]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, res)
            return res
        
        # the start or end element is found only once in the adjacentPairs
        end = 0
        for k in graph.keys():
            if len(graph[k]) == 1:
                end = k
                break
                
        visited = set([end])
        return dfs(end, [])