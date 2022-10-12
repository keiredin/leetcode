class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [1] * N
        
        for i in range(1,N):
            if arr[i] > arr[i-1]:
                dp[i] += dp[i-1]
                
        for j in range(N-2,-1,-1):
            if arr[j]> arr[j+1]:
                dp[j] += dp[j+1]
                
        answ = 0
        for i in range(1,N-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                answ = max(answ, dp[i])
                
        return answ
            
            