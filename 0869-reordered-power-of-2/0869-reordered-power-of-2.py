class Solution(object):
    def reorderedPowerOf2(self, n):
        count = Counter(str(n))
        
        for i in range(31):
            if Counter(str(1 << i)) == count:
                return True
        return False