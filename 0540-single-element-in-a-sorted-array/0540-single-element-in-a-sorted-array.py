class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-2  # hi starts from an even index so that hi^1 gives the next odd number
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == nums[mid^1]:
                lo = mid+1
            else:
                hi = mid-1
        return nums[lo]