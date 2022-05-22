class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)   # mapping charCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            
      
        return ans.values()
    
    # time O(m+n)
    # space O(m) + O(26)
        