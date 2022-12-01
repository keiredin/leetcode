class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        str1,str2 = 0,0
        
        for i in range(half):
            str1 += self.isVowel(s[i])
            str2 += self.isVowel(s[len(s) - i - 1])
        return str1 == str2
        
    def isVowel(self,char):
        return char in "aeiouAEIOU"
        