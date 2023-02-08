class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       

        freq = defaultdict(int)  # map of element to its last index
        start, end = 0, 0
        maxLen = 1
        distinct = 0    # cant pass 2

        while end < len(fruits):
            freq[fruits[end]] += 1
            if freq[fruits[end]] == 1: distinct += 1
            if distinct <= 2:
                maxLen = max(maxLen, end-start+1)
                
            while distinct > 2 and start < end:
                freq[fruits[start]] -= 1
                if freq[fruits[start]] == 0: distinct -= 1
                start += 1

                
            end += 1         
           
        return maxLen