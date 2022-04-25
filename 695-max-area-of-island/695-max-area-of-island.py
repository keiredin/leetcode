#path compression + union by rank
class UnionFind:
    def __init__(self,row,col):
        self.parent = {}
        self.size = {}
        
    
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
              
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid) 
        col = len(grid[0])
        uf = UnionFind(row,col)
        
        
        uf.parent = {(i, j): (i, j) for i in range(row) for j in range(col)}
        uf.size = {(i, j): grid[i][j] for i in range(row) for j in range(col)}
        
        in_bound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        direction_array = [[0,-1],[-1,0]]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    for d in direction_array:
                        newR, newC = r + d[0], c + d[1]
                        if in_bound(newR, newC) and grid[newR][newC] == 1:
                            uf.union((r, c), (newR, newC))
          
        return max(uf.size.values())
        