from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        p1,p2 = point
        self.points[(p1,p2)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point
        
        for (x2, y2),val in self.points.items():
            horLength, verLength = abs(x1 - x2), abs(y1 - y2)
            if horLength == verLength > 0:
                if (x1, y2) in self.points and (x2, y1) in self.points:
                    count += val * self.points[(x1, y2)] * self.points[(x2, y1)]
                    

        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)