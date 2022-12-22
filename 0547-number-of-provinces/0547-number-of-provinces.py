#path compression + union by rank
class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.provinceCount = size
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self,node1,node2):
        root1,root2 = self.find(node1), self.find(node2)
        
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
            
        elif self.rank[root2] > self.rank[root1]:
            self.root[root1] = root2
        else:
            self.root[root2] = root1
            self.rank[root1] += 1
            
        self.provinceCount -= 1
            
    def isSameGroup(self,node1,node2):
        return self.find(node1) == self.find(node2)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    if not uf.isSameGroup(i,j):
                        uf.union(i,j)
        return uf.provinceCount
                        
                
       
        
        
        