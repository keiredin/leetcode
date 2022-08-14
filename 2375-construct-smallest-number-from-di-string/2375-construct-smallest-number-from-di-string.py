class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        answ = [i for i in range(1, N+2)]
        
        for t in itertools.permutations(answ):
            for i in range(N):
                if t[i] > t[i+1]:
                    if pattern[i] == "I":
                        break
                else:
                    if pattern[i] == "D":
                        break
            
            else:
                return "".join(map(str,t))
        
                
        