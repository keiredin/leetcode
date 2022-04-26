class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        # count = Counter(nums)
        # for key in count:
        #     if count[key] > 1:
        #         return True
        # return False
        