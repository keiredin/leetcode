class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        totalNum = num
        num = str(num)
        k_buety = 0
        
        l,r = 0, k-1
        
        while r < len(num):
            curNum = int(num[l:r+1])
            
            if curNum and totalNum % curNum == 0:
                k_buety += 1
                
            l += 1
            r += 1
            
        return k_buety
                
        