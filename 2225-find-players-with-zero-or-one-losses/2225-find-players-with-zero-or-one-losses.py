class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnersCount = defaultdict(int)
        losersCount = defaultdict(int)
        
        for winner,loser in matches:
            winnersCount[winner] += 1
            losersCount[loser] += 1
    
    
        notLost = sorted(list(winner for winner in winnersCount.keys() if winner not in losersCount))
        lostOnes = sorted(list(key for key in losersCount.keys() if losersCount[key] == 1))
        
        return [notLost, lostOnes]
                
        