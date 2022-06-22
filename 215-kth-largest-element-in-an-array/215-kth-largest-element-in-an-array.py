class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * ele for ele in nums]
        heapify(nums)
        while nums and k > 1:
            heappop(nums)
            k -= 1
            
        return nums[0]*-1
        