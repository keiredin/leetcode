class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        cand = [(abs(a-x),a) for a in arr]
        heapify(cand)
        answ = []
        while k > 0:
            answ.append(heappop(cand)[1])
            k -= 1
        
        return sorted(answ)
        