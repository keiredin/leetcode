class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [
            (int(time.split(":")[0])*60 + int(time.split(":")[1]))
            for time in timePoints]
        
        times = sorted(times)
        for t in times.copy():
            if t < 12*60:
                times.append(t + 24*60)
                
        return min([(t2-t1) for t1, t2 in zip(times[:-1], times[1:])])



# class Solution:
#     def findMinDifference(self, timePoints: List[str]) -> int:
#         for i in range(len(timePoints)):
#             timePoints[i] = int(timePoints[i][0:2]) * 60 + int(timePoints[i][3:])
        
#         timePoints.sort()  
#         minn = 1440 # the max difference 24 * 60
#         print(timePoints)
        
#         for i in range(len(timePoints) - 1):
#             diff = timePoints[i+1]- timePoints[i]
#             minn = min(minn,diff)
        
#         diff = min(1440 - timePoints[-1], timePoints[-1] - timePoints[0])
#         minn = min(diff,minn)
#         return minn 
                       
        
        
            
            
                                                                 
                                                                 
                                                                 
                                                                 
                                                                                                                                                                                
                                                                 
                                                                 
                                    
        
        
        
        
        
        
        
        
            
        