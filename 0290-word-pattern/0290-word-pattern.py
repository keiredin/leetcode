class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charWordMap = defaultdict(str)
        usedWords = set()
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            curChar = pattern[i]
            if curChar in charWordMap:
                if charWordMap[curChar] != s[i]:
                    return False
            elif s[i] in usedWords:
                return False
            else:
                charWordMap[curChar] = s[i]
                usedWords.add(s[i])
        return True