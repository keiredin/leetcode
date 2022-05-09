class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            '2': ["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
        
        def backtrack(idx, curStr): # idx tell us what index we are at in the given digit string
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[idx]]:
                backtrack(idx+1, curStr + c)
                
        if digits:
            backtrack(0, "")
        
        return res
        
        