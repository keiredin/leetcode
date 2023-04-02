class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return self.isScrambleUtil(s1, s2, memo)

    def isScrambleUtil(self,s1: str, s2: str, memo: dict) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        n = len(s1)
        for k in range(1, n):
            if self.isScrambleUtil(s1[0:k], s2[0:k], memo) and self.isScrambleUtil(s1[k:], s2[k:], memo):
                memo[(s1, s2)] = True
                return True
            if self.isScrambleUtil(s1[0:k], s2[n-k:], memo) and self.isScrambleUtil(s1[k:], s2[0:n-k], memo):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False
