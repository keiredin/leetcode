class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            count += self.isStretchy(word,s)
            
        return count
    
    def isStretchy(self,word,s):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] != word[j]:
                break
            count_s, count_w = 1, 1
            
            #count consequetive characters in s
            while i < len(s) - 1 and s[i] == s[i+1]:
                i += 1
                count_s += 1
                
            #count consequetive characters in cur word
            while j < len(word) - 1 and word[j] == word[j+1]:
                j += 1
                count_w += 1
                
            
            if count_s < count_w or (count_s > count_w and count_s < 3):
                break
            i += 1
            j += 1
        if i == len(s) and j == len(word):
            return 1
        else:
            return 0
