class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        prefix = [*beans]
        


        for i in range(1,n):
            prefix[i] += prefix[i-1]

        res = (prefix[-1] - prefix[0]) - ((n-1) * beans[0])

        for i in range(1,n):
            leftSum = prefix[i-1]
            rightSum = prefix[-1] - prefix[i]
            rightSum -= (n-1-i) * beans[i]

            res = min(res, rightSum + leftSum)

        return res
