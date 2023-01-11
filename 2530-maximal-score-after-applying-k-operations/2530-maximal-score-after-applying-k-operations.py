class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapify(nums)
        # for i,num in enumerate(nums):
        #     heappush((num,i))
        
        score = 0
        while nums and k:
            num = heappop(nums) * -1
            score += num
            
            num = ceil(num / 3)
            if num:
                heappush(nums,num * -1)
            
            k -= 1
        return score
            
            
        