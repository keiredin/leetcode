class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        dec_stack = []
        
        for i in range(len(nums) * 2):
            i %= len(nums)
            while dec_stack and nums[dec_stack[-1]] < nums[i]:
                res[dec_stack.pop()] = nums[i]
                
            dec_stack.append(i)
            
        return res
            
        