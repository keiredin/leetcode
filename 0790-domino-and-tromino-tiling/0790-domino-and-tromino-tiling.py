class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 1e9 + 7
     
        # If N is less than 3
        if (N < 3):
            return N

        # Store all dp-states
        dp = [[0] * 3 for i in range(N + 1)]

        # Base Case
        dp[0][0] = dp[1][0] = 1
        dp[1][1] = dp[1][2] = 1

        # Traverse the range [2, N]
        for i in range(2, N + 1):

            # Update the value of dp[i][0]
            dp[i][0] = (dp[i - 1][0] +
                        dp[i - 2][0] +
                        dp[i - 2][1] +
                        dp[i - 2][2]) % MOD

            # Update the value of dp[i][1]
            dp[i][1] = (dp[i - 1][0] +
                        dp[i - 1][2]) % MOD

            # Update the value of dp[i][2]
            dp[i][2] = (dp[i - 1][0] +
                        dp[i - 1][1]) % MOD

        # Return the number of ways as
        # the value of dp[N][0]
        return int(dp[N][0])

        