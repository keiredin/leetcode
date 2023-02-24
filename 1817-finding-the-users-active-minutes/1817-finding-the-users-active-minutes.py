class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        idActiveMinuteMap = defaultdict(set)
       
        for Id,minute in logs:
            idActiveMinuteMap[Id].add(minute)
            
            
        dic = defaultdict(int)
        for key,val in idActiveMinuteMap.items():
            dic[len(val)] += 1
            
        answ = [0] * k
        
        for i in range(k):
            if i+1 in dic:
                answ[i] = dic[i+1]
        return answ
            
        