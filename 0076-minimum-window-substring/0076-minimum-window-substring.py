class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_window = {}
        answ_indexes = [-1,-1]
        minLength = inf
        seenLetters, neededLetters = 0,len(count_t)
        
        l,r = 0,0
        
        while r < len(s):
            count_window[s[r]] = 1 + count_window.get(s[r],0)
            
            if count_window[s[r]] == count_t[s[r]]:
                seenLetters += 1
                
            while seenLetters == neededLetters:
                if (r-l+1) < minLength:
                    answ_indexes = [l,r]
                    minLength = r-l+1
                    
                count_window[s[l]] -= 1
                    
                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                    seenLetters -= 1
                l += 1
                
            r += 1
            
        i,j = answ_indexes
        return s[i: j+1] if minLength != inf else ""
        