class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key in count:
            if count[key] > 1:
                return True
        return False
        