class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inc_stack = []
        
        for i in range(len(nums)-1,-1,-1):
            if inc_stack and inc_stack[-1] > nums[i]:
                for j in range(len(inc_stack)):
                    if inc_stack[j] > nums[i]:
                        inc_stack[j], nums[i] = nums[i], inc_stack[j]
                        break
                break
            inc_stack.append(nums[i])
        
        print(inc_stack)
        diff = len(nums) - len(inc_stack)
            
        for i in range(len(inc_stack)):
            nums[i+diff] = inc_stack[i]
            
        return nums
            
            
        
        
        
        