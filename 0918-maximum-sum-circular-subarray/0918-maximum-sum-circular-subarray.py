class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dq = deque([(0, -1)])  # (prefixSum, index), dq is the increasing queue
        ans = nums[0]
        preSumSoFar = 0
        for i in range(2*n):
            preSumSoFar += nums[i % n]
            if i - dq[0][1] > n:  # Remove if index of dq.front() is out range size `n`
                dq.popleft()
            ans = max(ans, preSumSoFar - dq[0][0])  # Get the minimum preSum from the front of the deque
            while dq and dq[-1][0] >= preSumSoFar:  # We want to keep smaller preSums and the latest `preSumSoFar` is smaller which is better than old ones, don't need to keep those old values.
                dq.pop()
            dq.append((preSumSoFar, i))
        return ans