class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0]) < 97:
            for i in range(1,len(word)-1):
                if (ord(word[i]) < 97 and ord(word[i+1]) >= 97) or (ord(word[i]) >= 97 and ord(word[i+1]) < 97):
                    return False
        else:
            for i in range(1,len(word)):
                if ord(word[i]) < 97:
                    return False
        return True
                
        