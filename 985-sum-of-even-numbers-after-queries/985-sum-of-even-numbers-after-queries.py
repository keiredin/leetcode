class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        answ = [0] * len(queries)
        for num in nums:
            if num % 2 == 0:
                evenSum += num
        
        for i in range(len(queries)):
            val,idx = queries[i]
            
            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
                
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            
            answ[i] = evenSum
            
        return answ