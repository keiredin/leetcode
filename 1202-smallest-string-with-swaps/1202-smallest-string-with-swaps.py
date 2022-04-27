class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
		
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
		# 1. Union-Find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)

		# 2. Grouping
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

		# 3. Sorting
        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)
    
    
#     The main idea here is to represent the string as a graph (indexes are nodes and pairs are edges). We can swap characters only if they connected with an edge. Since we can swap chars any amount of time within formed by edges groups, any char in such a group can be placed to any place within the group. That means we can simply sort chars within every group, and resulting string will be the lexicographically smallest one. So we do it in three steps:

# Form groups using Union-Find data structure
# Convert union-find to a hashmap with chars and indexes as values
# Sort chars and indeses for every groups and form the result
# Time: O(nlogn)
# Space: O(n)