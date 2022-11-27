class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp, res = defaultdict(int), 0
        
        for i in range(1, len(A)):
            for j in range(i):
                d = A[i] - A[j]
                res += dp[(j, d)]
                dp[(i, d)] += dp[(j, d)] + 1
        
        return res
        