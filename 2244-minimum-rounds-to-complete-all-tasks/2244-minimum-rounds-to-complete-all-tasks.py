class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        rounds = 0
        
        for num in count.keys():
            
            if count[num] < 2:
                return -1
            
            rounds += count[num] // 3
            count[num] %= 3
            
            if count[num] > 0:
                rounds += 1
                count[num] = 0
        
        return rounds