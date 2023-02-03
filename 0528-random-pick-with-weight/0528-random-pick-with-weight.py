class Solution:
    def __init__(self, w: List[int]):
        self.w = list(accumulate(w))
    
    def pickIndex(self):
        probability = randint(1, self.w[-1])
 
        best,l, r = 0, 0,len(self.w)-1
        while l < r:
            mid = l + (r-l)//2
            if probability > self.w[mid]:
                l = mid + 1
                best = l
            else:
                r = mid
                
        return best

 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()