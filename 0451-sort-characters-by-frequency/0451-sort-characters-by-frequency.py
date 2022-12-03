import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        l = []
        l[:0] = s
        count = Counter(l)
        l = [[-1*v,k] for k,v in count.items()]
        heapq.heapify(l)
        ans = []
        
        while l:
            s = heapq.heappop(l)
            string = s[0] * -1 * s[1]
            ans.append(string)
            
        return "".join(ans)
        