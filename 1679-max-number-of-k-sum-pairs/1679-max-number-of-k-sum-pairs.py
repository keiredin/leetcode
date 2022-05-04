class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operation = 0
        
        for num in nums:
            operation += min(count[num],count[k-num]) if num != k / 2 else count[num] // 2
            count[num],count[k-num] = 0,0
                
        return operation 