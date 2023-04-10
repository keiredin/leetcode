class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if(l%2 != 0):
            return False
        storeO = []
        openingP = "({["
        closingP = ")}]"
        for parenthesis in s:
            if parenthesis in openingP:
                storeO.append(parenthesis)
            elif parenthesis in closingP:
                if (storeO):
                    op = storeO[-1]
                    if(openingP.index(op) == closingP.index(parenthesis)):
                        storeO.pop()
                    else:
                        return False
                else:
                    return False
        return False if len(storeO)  else True        
                
        