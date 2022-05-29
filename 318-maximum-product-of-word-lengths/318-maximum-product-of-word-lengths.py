class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        
        bit_masks = [0] * n
        lengths = [0] * n
        
        for i in range(n):             
            for c in words[i]:
                bit_masks[i]|=1<<(ord(c) - ord('a')) # set the character bit            
            lengths[i]=len(words[i])
                        
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (bit_masks[i] & bit_masks[j]):
                    max_val=max(max_val, lengths[i] * lengths[j])
        
        return max_val 



# class Solution:
#     def maxProduct(self, words: List[str]) -> int:
#          return max([len(s1) * len(s2) for s1, s2 in combinations(words, 2)  if not (set(s1) & set(s2))], default=0)




# class Solution:
#     def maxProduct(self, words: List[str]) -> int:
#         n=len(words)                        
#         char_set = [set(words[i]) for i in range(n)] # precompute hashset for each word                                                  
#         max_val = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if not (char_set[i] & char_set[j]): # if nothing common
#                     max_val=max(max_val, len(words[i]) * len(words[j]))
        
#         return max_val 
        