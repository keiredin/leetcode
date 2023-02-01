class Solution:
    def earliestFullBloom(self, plantTime: List[int],
                          growTime: List[int]) -> int:
        
        curPlantingTime = 0
        result = 0
        plantGrowTimePair = []
        
        for i in range(len(plantTime)):
            plantGrowTimePair.append((growTime[i],plantTime[i]))
        
        plantGrowTimePair.sort()
   
        for i in range(len(plantTime))[::-1]:
            curPlantingTime += plantGrowTimePair[i][1]
            result = max(result, curPlantingTime + plantGrowTimePair[i][0])
     
        return result