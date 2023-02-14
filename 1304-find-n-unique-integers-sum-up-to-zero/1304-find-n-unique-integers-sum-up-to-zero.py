class Solution:
    def sumZero(self, n: int) -> List[int]:
        answ = []
        mod = n % 2
        n = n // 2
        while n > 0:
            answ.append(n*-1)
            answ.append(n)
            n -= 1
            
        if mod:
            answ.append(0)
            
        return answ
        