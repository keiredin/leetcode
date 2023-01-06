class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        idx = 0
        count = 0
        while idx < len(costs) and coins:
            if costs[idx] > coins:
                return count
            coins -= costs[idx]
            idx += 1
            count += 1
            
        return count