class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left,right = 0,0
        res, total = 0,0
        
        while right < n:
            total += nums[right]
            
            if nums[right] * (right -left + 1) > total + k:
                total -= nums[left]
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
            
            
            
            
        return res
        
#         for i in range(n):
#             for j in range(i+1,n):
#                 temp = nums[j]
#                 while( (k>0) and (temp < nums[i]) ):
#                     temp += 1
#                     k -= 1
                
#                     if(temp == nums[i]):
#                         count[i] += 1
                    
#         max_f = count[nums[0]]           
#         for key in nums:
#             if count[key] > max_f:
#                 max_f = nums[key]
                
#         return max_f
                
                