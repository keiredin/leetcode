class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        
        for t in time:
            mod = t % 60
            if mod in count:
                res += count[mod]
                
            if mod> 0:
                count[60 - mod] += 1
            else:
                count[mod] += 1
            
        return res
            
            
        