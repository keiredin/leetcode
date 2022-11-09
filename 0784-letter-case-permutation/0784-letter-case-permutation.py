class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answ = []
        
        def backtrack(curStr, s, curIdx):
            if curIdx == len(s):
                answ.append(curStr)
                return
            
            
            if 47 < ord(s[curIdx]) < 58:
                curStr += s[curIdx]
                backtrack(curStr, s, curIdx + 1)
            else:
                # append lowercase
                lowerCase = curStr
                lowerCase += s[curIdx].lower()
                backtrack(lowerCase, s, curIdx + 1)
                
                #aapend uppercase
                uppercase = curStr
                uppercase += s[curIdx].upper()
                backtrack(uppercase, s, curIdx + 1)
                
        
        backtrack("", s, 0)
        return answ
        
        
        
