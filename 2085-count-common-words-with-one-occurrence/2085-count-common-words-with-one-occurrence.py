class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        answ = 0
        
        for word in count1:
            if word in count2 and count1[word] == 1 and count2[word] == 1:
                answ += 1
                
        return answ