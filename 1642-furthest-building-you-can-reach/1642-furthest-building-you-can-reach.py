import heapq as hq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lastBuilding = len(heights)-1
        min_heap = []
        for i in range(lastBuilding):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            else:
                heappush(min_heap, diff)
                if ladders > 0:
                    ladders -= 1
                elif bricks >= min_heap[0]:
                    bricks -= min_heap[0]
                    heappop(min_heap)
                else:
                    return i
                
        return lastBuilding


# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         heapify(heights)
#         prev = heappop(heights)
        
#         while (ladders or bricks) and heights:
#             print(prev)
#             curr = heappop(heights)
#             print(curr,"curr")
#             diff = curr - prev
#             if diff > 0:
#                 if bricks > 0 and bricks - diff >= 0:
#                     bricks -= diff
#                 else:
#                     ladders -= 1
                    
            
#             prev = heappop(heights)
#         print(heights)     
#         return prev
        