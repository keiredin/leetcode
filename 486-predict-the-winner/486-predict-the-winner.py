class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.winner(nums, 0, len(nums)-1, 1) >= 0
    
    def winner(self,nums,s, e, turn):
        if s == e:
            return turn * nums[s]
        
        a = turn * nums[s] + self.winner(nums, s+1, e, -turn)
        b = turn * nums[e] + self.winner(nums, s, e-1, -turn)
        
        return turn * max(turn * a, turn * b)