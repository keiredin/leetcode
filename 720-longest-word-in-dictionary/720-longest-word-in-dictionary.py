class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordsSet = set(words)
        words.sort()
        answ = ""
        for word in words:
            l,r = 0,1
            while r < len(word):
                if word[l:r] not in wordsSet:
                    break
                r += 1
            else:
                if len(word) > len(answ):
                    answ = word
        return answ
                
        