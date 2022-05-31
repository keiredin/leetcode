# # Approach 1: Set
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         need = 1 << k
#         got = set()

#         for i in range(k, len(s)+1):
#             tmp = s[i-k:i]
#             if tmp not in got:
#                 got.add(tmp)
#                 need -= 1
#                 # return True when found all occurrences
#                 if need == 0:
#                     return True
#         return False  
    
# # Since there are two possible char for each place: 0 or 1, there will be 2^k possible binary code.
# # 1 << k is the same as 2^k 
# # time O(NK) and Space O(NK)


# Approach 2: Hash

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False]*need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False
    
# time O(N) and space O(2^k)