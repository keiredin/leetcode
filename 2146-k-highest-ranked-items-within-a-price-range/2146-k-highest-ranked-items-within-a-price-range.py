class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        dir_arr = [[-1,0],[1,0],[0,-1],[0,1]]
        inBound = lambda r,c : 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        sRow,sCol = start
        startPrice = grid[sRow][sCol]
        
        queue = [[0,startPrice,sRow,sCol]]
        visited = set()
        visited.add((sRow,sCol))
        
        res = []
        while queue:
            dist,price,row,col = heappop(queue)
            if pricing[0] <= price <= pricing[1]:
                res.append([row,col])
                if len(res) >= k:
                    break
                
            
            for d in dir_arr:
                newR,newC = row+d[0], col + d[1]
                
                if inBound(newR,newC) and (newR,newC) not in visited:
                    curPrice = grid[newR][newC]
                    
                    # if not a wall
                    if curPrice:
                        heappush(queue,[dist+1, curPrice, newR, newC])
                        visited.add((newR,newC))
        return res
                    
                        
                
        