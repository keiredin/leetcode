class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        answ = 0
        while maxDoubles and target > 1:
            if target % 2 == 1:
                target -= 1
                answ += 1
                
            target //=2
            answ += 1
            maxDoubles -= 1
            
        return answ + (target-1)