class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.rank = []
    
        count = defaultdict(int)
        curr_max = persons[0]

        for p in persons:
            count[p] += 1
            
            if count[p] >= count[curr_max]:
                self.rank.append(p)
                curr_max = p
            else:
                self.rank.append(curr_max)
                
        print(self.rank)
    
    def q(self, t: int) -> int:
        l,r = 0, len(self.times)-1
        while l <= r:
            mid = (l + r) // 2
            if t == self.times[mid]:
                return self.rank[mid]   
            elif t > self.times[mid]:
                l = mid + 1
            else :
                r = mid - 1
                
        return self.rank[r] 
                
            # if l > r:
            #     return self.winner(self.persons,l) if l > 0 else self.winner(self.persons,l+1)
        
            
            
            
            
        
    # def winner(self,person,idx):
    #     # count = Counter(person[:idx])
    #     leading, count = person[0], {}
    #     for i in person[:idx]:
    #         if i in count:
    #             count[i] += 1
    #         else:
    #             count[i] = 1
    #         if count[i] >= count[leading]:
    #             leading = i
    #     return leading
    
    
    # cur, repo = persons[0], {}
    #     for i in persons:
    #         if i in repo:
    #             repo[i] += 1
    #         else:
    #             repo[i] = 1
    #         if repo[i] >= repo[cur]:
    #             self.leaderboard.append(i)
    #             cur = i
    #         else:
    #             self.leaderboard.append(cur)
        
        
    
    
                
      
   

                
    
        



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)