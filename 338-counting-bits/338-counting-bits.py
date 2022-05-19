class Solution:
    def countBits(self, n: int) -> List[int]:
        answ = []
        for i in range(n+1):
            binary = bin(i)
            answ.append(binary.count('1'))
            
        return answ
        