class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        charIdx1, charIdx2 = 0,0   # inner pointers for the strings
        wordIdx1, wordIdx2 = 0, 0  # outer pointer to iterate over the array
        
        while wordIdx1 < len(word1) and wordIdx2 < len(word2):
            curWord1 = word1[wordIdx1]
            curWord2 = word2[wordIdx2]
            
            if curWord1[charIdx1] != curWord2[charIdx2]:
                return False
            
            
            if charIdx2 < len(curWord2)-1:
                charIdx2 += 1
            else:
                charIdx2 = 0
                wordIdx2 += 1
                
            if charIdx1 < len(curWord1)-1:
                charIdx1 += 1
            else:
                charIdx1 = 0
                wordIdx1 += 1
                
        return wordIdx1 == len(word1) and wordIdx2 == len(word2)
    
#     def processInternalIndex(self,charIdx, word):
#         if charIdx < len(word)-1:
#             charIdx += 1
#         else:
#             charIdx = 0
            
#         return charIdx
                
            
                
                
            