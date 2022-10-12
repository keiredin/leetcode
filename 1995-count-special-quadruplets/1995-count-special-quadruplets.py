class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        answ = 0
        for i1 in range(N):
            for i2 in range(i1+1,N):
                for i3 in range(i2+1, N):
                    for i4 in range(i3+1, N):
                        if nums[i1] + nums[i2] + nums[i3] == nums[i4]:
                            answ += 1
        return answ
                
            
        