class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        curMin,curMax = nums[0],nums[-1]
        operations = 0
        
        for i in range(len(nums)):
            curMin = nums[i]
            if curMin > 0:
                for j in range(i,len(nums)):
                    if nums[j] > 0:
                        nums[j] -= curMin
                    curMax = max(curMax, nums[j])

                    if curMax <= 0:
                        return operations

                operations += 1

        return operations      
                
            
            
        