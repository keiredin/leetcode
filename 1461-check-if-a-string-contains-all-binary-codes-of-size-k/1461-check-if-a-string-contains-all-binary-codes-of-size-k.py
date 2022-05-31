# Approach 1: Set
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False  
    
# Since there are two possible char for each place: 0 or 1, there will be 2^k possible binary code.
# 1 << k is the same as 2^k 