class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_index, last_index, count = {}, {}, {}
        
        for i, num in enumerate(nums):
            if num not in first_index: first_index[num] = i
            last_index[num] = i
            count[num] = count.get(num, 0) + 1

        min_window = len(nums)
        max_frequency = max(count.values())
        
        for num in count:
            if count[num] == max_frequency:
                min_window = min(min_window, last_index[num] - first_index[num] + 1)

        return min_window