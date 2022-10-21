class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for idx,num in enumerate(nums):
            if num in hashmap:
                if abs(hashmap[num] - idx) <= k:
                    return True
            hashmap[num] = idx
            
        return False
        