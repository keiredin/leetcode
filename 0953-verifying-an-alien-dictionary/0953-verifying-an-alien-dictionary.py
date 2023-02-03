class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charOrderMap = defaultdict(int)
        for i,char in enumerate(order):
            charOrderMap[char] = i
        
        for i in range(1,len(words)):
            prev = words[i-1]
            cur = words[i]
            
            j = 0
            while j < min(len(prev), len(cur)):
                if charOrderMap[prev[j]] > charOrderMap[cur[j]]:
                    return False
                elif charOrderMap[prev[j]] != charOrderMap[cur[j]]:
                    break
                j += 1
            
            # check condition like (["apple","app"])
            if j >= min(len(prev), len(cur)):
                if len(prev) > len(cur):
                    return False        
                
        return True