#path compression + union by rank
class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.rank = [1] * n
        self.count = n
        
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
                
            self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        # print(uf.parent)            
        return uf.count
        
        
        