class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        count = Counter(nums)
        
        for curNum in nums:
            if count[curNum]:
                for i in range(1, k):
                    if count[curNum + i] >= count[curNum] :
                        count[curNum + i] -= count[curNum]
                    else:
                        return False
                count[curNum] = 0
        
        return True