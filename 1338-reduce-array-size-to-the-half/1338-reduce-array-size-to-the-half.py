class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        max_heap = [(-x[1],x[0]) for x in count.items()]
        heapify(max_heap)
        

        l = len(arr) // 2
        answ = set()
        while l > 0:
            most_frequent = heappop(max_heap)
            l -= (most_frequent[0] * -1)
            answ.add(most_frequent[1])
       
        
        return len(answ)
        

        