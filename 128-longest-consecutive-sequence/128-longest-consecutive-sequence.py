class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(i for i in nums)        
        longest = 0
        for i in nums:
            count = 0
            if i - 1 in numSet:
                continue

            while i in numSet:
                count += 1
                i += 1
            longest = max(longest,count)     
            
        return longest
            
                
        