import heapq as hq
class MedianFinder:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        

    def addNum(self, num: int) -> None:
        if len(self.heap1) == 0 and len(self.heap2) == 0:
            hq.heappush(self.heap1,num * -1)
        
        
        elif len(self.heap1) <= len(self.heap2):
            if num > self.heap2[0]:
                hq.heappush(self.heap1, hq.heappop(self.heap2)*-1)
                hq.heappush(self.heap2,num)
            else:
                hq.heappush(self.heap1,num * -1)

        else:
            if num < self.heap1[0] * -1:
                hq.heappush(self.heap2, hq.heappop(self.heap1)*-1)
                hq.heappush(self.heap1,num * -1)

            else:
                hq.heappush(self.heap2,num)


    def findMedian(self) -> float:
        l1 = len(self.heap1)
        l2 = len(self.heap2)
        if l1 == l2:
            a1 = self.heap1[0] * -1
            a2 = self.heap2[0]
            median = (a1 + a2) / 2
            return median
        elif l1 > l2:
            return (self.heap1[0] * -1) / 1

        else:
            return self.heap2[0] / 1
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# def runningMedian(a):
#     # Write your code here
#     answ = []
#     lower,upper = [],[]
#     for num in a:
#         pushElement(num,lower,upper)
#         median = calcMedian(lower,upper)
#         answ.append(median)
#     return answ
#         # answ.append([median])
#         # print("{:.1f}".format(median))
        
# def pushElement(ele,heap1,heap2):
    
#     if len(heap1) == 0 and len(heap2) == 0:
#         hq.heappush(heap1,ele * -1)
        
        
#     elif len(heap1) <= len(heap2):
#         if ele > heap2[0]:
#             hq.heappush(heap1, hq.heappop(heap2)*-1)
#             hq.heappush(heap2,ele)
#         else:
#             hq.heappush(heap1,ele * -1)
            
#     else:
#         if ele < heap1[0] * -1:
#             hq.heappush(heap2, hq.heappop(heap1)*-1)
#             hq.heappush(heap1,ele * -1)
            
#         else:
#             hq.heappush(heap2,ele)
            
#     # print(heap1)
#     # print(heap2)
            
# def calcMedian(heap1,heap2):
#     l1 = len(heap1)
#     l2 = len(heap2)
#     if l1 == l2:
#         a1 = heap1[0] * -1
#         a2 = heap2[0]
#         median = (a1 + a2) / 2.0
#         return median
#     elif l1 > l2:
#         return (heap1[0] * -1) / 1.0
        
#     else:
#         return heap2[0] / 1.0