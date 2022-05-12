class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c = {}
        c2={}   
        
        for i in range(len(s)):
            if s[i] not in c:
                c[s[i]] = t[i]
    
            else:
                if c[s[i]] != t[i]:
                    return False
        for i in range(len(t)):
            if t[i] not in c2:
                c2[t[i]] = s[i]
            else:
                if c2[t[i]] != s[i]:
                    return False
        
        return True
                
        