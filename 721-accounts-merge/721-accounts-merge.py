#path compression + union by rank
class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.rank = [1] * n
        self.groupCount = n
        
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
                
            self.groupCount -= 1
                


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        
        mapEmailToAccountIdx = {}  # key=email and value=the index of the account the email first appeared in
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                if account[j] not in mapEmailToAccountIdx:
                    mapEmailToAccountIdx[account[j]] = i
                else:
                    uf.union( i, mapEmailToAccountIdx[account[j]] )
        
        
        for i in range(len(accounts)): # to be safe
            uf.find(i)
            
        answer = defaultdict(set)
        for c, p in uf.parent.items():
            answer[p].update(set(accounts[c][1:]))
        
        return [[accounts[key][0]] + sorted(list(value)) for key, value in answer.items()]
        