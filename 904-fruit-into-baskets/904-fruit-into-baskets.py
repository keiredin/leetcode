class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 0:
            return 0

        hashMap = defaultdict()  # map of element to its last index
        start, end = 0, 0
        maxLen = 1

        while end < len(fruits):
            
            if len(hashMap) <= 2:
                hashMap[fruits[end]] = end
                
            if len(hashMap) > 2:
                minn = len(fruits) - 1
                
                for key in hashMap:
                    minn = min(minn,hashMap[key])
                start = minn + 1
                del hashMap[fruits[minn]]
                
            end += 1 
            maxLen = max(maxLen, end - start)           
           
        return maxLen
                    
            
                
            