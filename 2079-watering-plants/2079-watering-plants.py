class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curCapacity = capacity
        
        for i in range(len(plants)):
            if plants[i] > curCapacity:
                steps += ((i) * 2)
                curCapacity = capacity
            
            steps += 1
            curCapacity -= plants[i]
            
            
        return steps