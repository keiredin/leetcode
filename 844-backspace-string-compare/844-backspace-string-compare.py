class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.parse(s) == self.parse(t)
    
    def parse(self,string):
        res = []
        for s in string:
            if s == '#':
                if res:
                    res.pop()
            else:
                res.append(s)
       
        return res