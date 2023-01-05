class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        valid_range = points[0]
        arrows = 1
        
        for b in points[1:]:
            if valid_range[0] <= b[0] <= valid_range[1]:
                valid_range[0] = max(valid_range[0],b[0])
                valid_range[1] = min(valid_range[1],b[1])
            else:
                arrows += 1
                valid_range = b
                
        return arrows
                
                
        