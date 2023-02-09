from sortedcontainers import SortedList
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = defaultdict(lambda : -1)  
        q = deque()  
       
        s = SortedList() 
        cnt = Counter()  
        
        ans = 0
        for r,v in enumerate(nums):
            q.append(r)
            cnt[v] += 1
            s.discard(right[v])  
            s.add(r)  
            right[v] = max(right[v],r) 
            while len(cnt)>k:
                l = q.popleft()  
                s.discard(l)               
                x = nums[l]
                cnt[x] -= 1
                if not cnt[x]:
                    del cnt[x]
            if len(cnt) == k:
                ans += s[0] - q[0]+1
        return ans

