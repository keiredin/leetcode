class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)-1 
        l,r = 0, n
        hIndex = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            if citations[mid] <= n - mid:
                l = mid + 1
            else:
                hIndex = max(hIndex, n-mid+1)
                r = mid - 1
            
                
        return hIndex
            
            