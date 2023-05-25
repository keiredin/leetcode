class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for num in bills:
            if num == 5:
                count[num] += 1
            elif num == 10:
                if count[5] < 1:
                    return False
                count[num] += 1
                count[5] -= 1
            else:
                if count[5] >= 1 and count[10] >= 1:
                    count[5] -= 1
                    count[10] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True
        