class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        unique = set(words)

        def dfs(word):  
            if word not in dp:               
                maxLen = 1
                for i in range(len(word)):
                    prev = word[:i] + word[i+1:]
                    if prev in unique:
                        maxLen = max(maxLen, 1 + dfs(prev))

                dp[word] = maxLen
            return dp[word]
        
        res = 0
        for word in words:
            res = max(res,dfs(word))
        
        return res
