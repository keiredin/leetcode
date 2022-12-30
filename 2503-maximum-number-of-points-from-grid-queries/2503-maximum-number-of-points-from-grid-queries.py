class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        valIndexMap = defaultdict(list)
        answ = [0] * len(queries)
        
       
        
        dir_arr  = [[1,0],[-1,0],[0,1],[0,-1]]
        inBound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0]) 
        
        
        for i,val in enumerate(queries):
            valIndexMap[val].append(i)
            
        queries.sort()
        
        
        
            
        queue = [[grid[0][0], 0, 0]]
        visited = set()
        visited.add((0,0))
        
        curSum = 0
        indx = 0
        while queue and indx < len(queries):
            curQuerie = queries[indx]
            cur,i,j = heappop(queue)
            if cur < curQuerie:
                curSum += 1
                for d in dir_arr:
                    newI,newJ = i + d[0], j + d[1]
                    
                    if inBound(newI,newJ) and (newI,newJ) not in visited:
                        visited.add((newI,newJ))
                        heappush(queue,[grid[newI][newJ],newI,newJ])
                    
            else:
                curQuerieIndex = valIndexMap[curQuerie].pop()
                answ[curQuerieIndex] = curSum
                heappush(queue,[cur,i,j] )
                indx += 1
                
        # if heap is empty but not the query
        if indx < len(queries):
            curQuerie = queries[indx]
            curQuerieIndex = valIndexMap[curQuerie].pop()
            answ[curQuerieIndex] = curSum
        
        for key,indList in valIndexMap.items():
            if indList:
                for index in indList:
                    answ[index] = curSum
                
        return answ

            
                
            
            
        
        