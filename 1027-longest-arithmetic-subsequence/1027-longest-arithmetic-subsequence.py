class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        longest = 0
        n = len(nums)
        indexLengthMap = [{} for i in range(n)] 

        
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev = indexLengthMap[j].get(diff, 1)   # what was longest till j with difference diff
                longest = max(prev + 1, longest)
                indexLengthMap[i][diff] = prev + 1   

        return longest
        