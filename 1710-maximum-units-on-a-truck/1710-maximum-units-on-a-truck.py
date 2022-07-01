class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse=True) # sort the array by unit decreasingly
        
        answ = 0
        for i in range(len(boxTypes)):
            if truckSize >= boxTypes[i][0]:
                answ += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                answ += truckSize * boxTypes[i][1]
                break
        return answ
                
        