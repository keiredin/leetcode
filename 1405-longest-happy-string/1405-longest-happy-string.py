class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "",[]
        
        for freq, char in [(-a,'a'),(-b, 'b'), (-c, 'c')]:
            if freq:
                heappush(maxHeap, (freq,char))
                
        while maxHeap:
            freq,char = heappop(maxHeap)
            
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                freq2,char2 = heappop(maxHeap)
                res += char2
                
                freq2 += 1
                if freq2:
                    heappush(maxHeap, (freq2,char2))
            else:
                res += char
                freq += 1
                
            if freq:
                heappush(maxHeap, (freq, char))
                    
        return res
        