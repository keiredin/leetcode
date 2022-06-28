class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        freq_lst = [-freq[key] for key in freq]
        heapify(freq_lst)
        dec_count = 0
        
        
        
        while len(freq_lst) > 1:
            top_ele = -heappop(freq_lst)
            
            if -freq_lst[0] == top_ele:
                dec_count += 1
                top_ele -= 1
                if top_ele > 0:
                    heappush(freq_lst, -top_ele)
            
        return dec_count        