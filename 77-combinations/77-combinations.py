class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answ = []
        def backtrack(i,lst):
            if len(lst) == k:
                answ.append(tuple(lst))
                return
                
            for j in range(i+1,n+1):
                lst.append(j)
                backtrack(j,lst)
                lst.pop()
          
        backtrack(0,[])
        return answ
        