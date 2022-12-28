class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answ = []
        s = set()
        

        
        for i in range(n):
            for j in range(i+1,n):
                left,right = j+1,n-1
                exp = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] > exp:
                        right -= 1
                    elif nums[left] + nums[right] < exp:
                        left += 1
                    else:
                        cur  = [nums[i],nums[j],nums[left],nums[right]]
                        if tuple(cur) not in s:
                            s.add(tuple(cur))
                            answ.append(cur)
                        left += 1
                        right -= 1
                
            
        return answ
        