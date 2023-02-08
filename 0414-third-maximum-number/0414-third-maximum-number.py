class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x1,x2,x3 = -inf,-inf,-inf
        
        for num in nums:
            if num > x1:
                x1,x2,x3 = num, x1, x2
            elif num != x1 and num > x2:
                x2,x3 = num,x2
            elif num != x1 and num != x2 and num > x3:
                x3 = num
                
        return x3 if x3 != -inf else x1
        