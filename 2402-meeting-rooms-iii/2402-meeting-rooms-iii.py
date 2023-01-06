class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free_rooms = [i for i in range(1,n)]
        heapify(free_rooms)
        occupiedRooms = [(meetings[0][1],0)]
        heapify(occupiedRooms)
        count = [0] * n
        count[0] += 1
        # maxx = count[0]
        
        for m in meetings[1:]:
            start,end = m[0],m[1]
            duration = end-start
            
            while occupiedRooms and start >= occupiedRooms[0][0]:
                heappush(free_rooms, heappop(occupiedRooms)[1])
            
            if free_rooms:
                cur = heappop(free_rooms)
                count[cur] += 1
                heappush(occupiedRooms,(end,cur))
            else:
                cur = heappop(occupiedRooms)
                count[cur[1]] += 1
                heappush(occupiedRooms, (cur[0]+duration, cur[1]))
                
       
        return count.index(max(count))
            
            
            
            
        
        