class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        # print(self.minHeap, self.maxHeap)
        if self.minHeap or  self.maxHeap:
            if len(self.maxHeap) > len(self.minHeap):
                if self.maxHeap[0] * -1 > num:
                    heappush(self.minHeap, heappop(self.maxHeap) * -1)
                    heappush(self.maxHeap, -1*num)
                else:
                    heappush(self.minHeap, num)
                    
            elif len(self.minHeap) > len(self.maxHeap):
                if self.minHeap[0] < num:
                    heappush(self.maxHeap, heappop(self.minHeap) * -1)
                    heappush(self.minHeap, num)
                else:
                    heappush(self.maxHeap, num * -1)
            else:
                
                if num > self.minHeap[0]:
                    heappush(self.minHeap, num)
                else:
                    heappush(self.maxHeap, num * -1)
        else:
            heappush(self.minHeap, num)
                
            
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        else:
            num1 = self.minHeap[0]
            num2 = self.maxHeap[0] * -1
            return (num1 + num2) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()