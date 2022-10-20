class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        
        for curNum in hand:
            if count[curNum]:
                for i in range(1, groupSize):
                    if count[curNum + i] >= count[curNum] :
                        count[curNum + i] -= count[curNum]
                    else:
                        return False
                count[curNum] = 0
        
        return True
                        
                    
            
            
        