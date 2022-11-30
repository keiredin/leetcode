class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        uniqueCount = set()
        
        for key,val in count.items():
            if val in uniqueCount:
                return False
            uniqueCount.add(val)
        
        return True
            
        