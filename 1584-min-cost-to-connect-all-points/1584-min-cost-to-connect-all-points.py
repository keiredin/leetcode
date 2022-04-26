class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.rank = [1] * n
        self.edge = 0
        self.cost = 0
        
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2,weight):
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
                
            self.edge += 1
            self.cost += weight
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        mapPoint2weight = {}
        
        # Calculate the weights of all edges and sort the weights
        for i in range(n) :
            point1 = (points[i][0],points[i][1])
            for j in range(i+1,n):
                currP = (points[j][0],points[j][1])
                
                edgeWeight = abs(currP[0] - point1[0]) + abs(currP[1] - point1[1])  # manhattan distance
                mapPoint2weight[(i,j)] = edgeWeight
                
        sortedPointToWeight = sorted(mapPoint2weight.items(), key=lambda item: item[1])
                
               
        # Build a minimum spanning tree 
        for point,weight in sortedPointToWeight:
            uf.union(point[0],point[1],weight)
            if uf.edge == n-1:
                break # break if all points are added - inorder to prevent cycle
        return uf.cost
                
                
                
        

        