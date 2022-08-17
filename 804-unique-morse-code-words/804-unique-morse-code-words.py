class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letterMorceMap = defaultdict(str)
        for i in range(26):
            letterMorceMap[chr(97+i)] = morseCode[i]
        
            
        answ = defaultdict(int)
        for word in words:
            cur_res = ""
            for char in word:
                cur_res += letterMorceMap[char]
            
            if cur_res:
                answ[cur_res] += 1
           
        

        res =  0
        for key in answ:
            res += 1
            
        return res
        
                
        