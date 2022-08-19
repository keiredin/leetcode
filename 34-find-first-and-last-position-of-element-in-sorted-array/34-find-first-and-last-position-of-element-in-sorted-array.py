class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(target,direction):
            l,r = 0,len(nums)-1 
            curPos = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    curPos = mid
                    if direction == 'left':
                        r = mid-1
                    else:
                        l = mid + 1
            return curPos
                        
        left_index = binarySearch(target,'left')
        last_index = binarySearch(target,'last')
        
        return [left_index, last_index]
                    
            