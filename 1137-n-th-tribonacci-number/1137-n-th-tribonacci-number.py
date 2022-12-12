class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n== 2:
            return 1
        
        n1,n2,n3 = 0,1,1
        
        for i in range(3,n+1):
            temp = n1 + n2 + n3
            n1,n2,n3 = n2,n3,temp
            
        return n3

        