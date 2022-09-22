class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        left = 0
        
        while left < len(s):
            fast = left + 2*k
            
            if left + k - 1 < len(s):
                for i in range(left+k-1,left-1,-1):
                    res.append(s[i])
                    
                res.append(s[left+k: fast])
            else:
                for i in range(len(s)-1,left-1,-1):
                    res.append(s[i])
            left = fast
        return ''.join(res)
        