class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        ageScorePair = []
        for i in range(n):
            ageScorePair.append((ages[i], scores[i]))
        ageScorePair.sort(key=lambda x:(x[0], x[1]))
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.findMaxScore(dp, ageScorePair, -1, 0)

    def findMaxScore(self, dp, ageScorePair, prev, index):
        if index == len(ageScorePair):
            return 0

        if dp[prev + 1][index] != -1:
            return dp[prev + 1][index]

        if prev == -1 or ageScorePair[index][1] >= ageScorePair[prev][1]:
            dp[prev + 1][index] = max(self.findMaxScore(dp, ageScorePair, prev, index + 1), ageScorePair[index][1] + self.findMaxScore(dp, ageScorePair, index, index + 1))
            return dp[prev + 1][index]


        dp[prev + 1][index] = self.findMaxScore(dp, ageScorePair, prev, index + 1)
        return dp[prev + 1][index]