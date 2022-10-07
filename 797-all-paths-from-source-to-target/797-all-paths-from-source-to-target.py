class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def backtrack(node,curList):
            if node == len(graph) - 1:
                ans.append(tuple(curList))
            
            for neighbor in graph[node]:
                curList.append(neighbor)
                backtrack(neighbor, curList)
                curList.pop()
                
        backtrack(0,[0])
        return ans
                
        