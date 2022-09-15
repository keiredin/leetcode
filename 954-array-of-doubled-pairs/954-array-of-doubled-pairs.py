class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        n = len(arr)
        if(n%2 != 0):
            return []
        count = Counter(arr)
        arr.sort()
        res = 0
        
        for num in arr:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                res += 1
            elif num != 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                res += 1
        print(res)       
        return True if res == n // 2 else False
        