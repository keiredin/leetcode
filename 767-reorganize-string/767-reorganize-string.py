class Solution:
    def reorganizeString(self, S):
        res, c = [], Counter(S)
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        prevChar_count, prev_char = 0, ''
        
        while pq:
            count, char = heapq.heappop(pq)
            res += [char]
            if prevChar_count < 0:
                heapq.heappush(pq, (prevChar_count, prev_char))
            count += 1
            prevChar_count, prev_char = count, char
            
        res = ''.join(res)
        
        if len(res) != len(S): return ""
        return res
                    
            
        