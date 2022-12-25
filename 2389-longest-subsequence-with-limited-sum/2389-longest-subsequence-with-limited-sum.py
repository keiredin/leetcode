class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answ = [0] * len(queries)
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        
        
        for j in range(len(queries)):
            for i in range(len(nums)-1,-1,-1):
                if nums[i] <= queries[j]:
                    answ[j] = i+1
                    break
                    
        return answ
        