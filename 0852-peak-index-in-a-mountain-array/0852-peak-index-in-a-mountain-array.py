class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr) - 1
        l,r = 0,n
        
        while l <= r:
            mid = (l+r) // 2
            
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid-1] > arr[mid]:
                r = mid
            else:
                l = mid + 1
                
        return r
        