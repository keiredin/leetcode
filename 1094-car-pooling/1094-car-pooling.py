class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        lst = []
        
        for i in range(len(trips)):
            p,s,e = trips[i]
            
            while lst and lst[0][0] <= s:
                capacity += heappop(lst)[1]
            
            if p <= capacity:
                capacity -= p
                heappush(lst, [e, p]) 
            else:
                return False
            
        return True
        
                
            
            
        