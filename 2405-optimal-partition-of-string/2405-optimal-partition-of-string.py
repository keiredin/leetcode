class Solution:
    def partitionString(self, s: str) -> int:
        res=0
        hashset=set()
        for i in range(len(s)):
            if s[i] not in hashset:
                hashset.add(s[i])
            else:
                res+=1
                hashset.clear()
                hashset.add(s[i])
        if len(list(hashset))==0:
            return res
        
        return res+1
        