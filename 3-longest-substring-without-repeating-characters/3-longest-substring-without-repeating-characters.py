class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end = 0,0
        maxS = 0
        curr = {}
        
        while end < len(s):
            if s[end] not in curr:
                curr[s[end]] = end
            
            else:
                maxS = max(maxS, end-start)
                idx = curr[s[end]]
                # remove all keys in the dict that have value 
                #that are to the left of the element to be removed from the window
                curr = {key : val for key, val in curr.items() if not (isinstance(val, int) and (val < idx))}
                start = idx+1
                curr[s[end]] = end
                
            end += 1
        maxS = max(maxS, end-start)
        return maxS
            
        