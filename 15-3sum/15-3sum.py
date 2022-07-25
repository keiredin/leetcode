class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answ = []
        s = set()
        
        for i in range(n):
            left,right = i+1,n-1
            exp = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] > exp:
                    right -= 1
                elif nums[left] + nums[right] < exp:
                    left += 1
                else:
                    cur  = [nums[i],nums[left],nums[right]]
                    if tuple(cur) not in s:
                        s.add(tuple(cur))
                        answ.append(cur)
                    left += 1
                    right -= 1
                
            
        return answ
                        
                
                
                
        