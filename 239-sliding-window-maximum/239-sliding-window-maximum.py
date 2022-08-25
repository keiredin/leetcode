class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answ = []
        valdec_queue = collections.deque()
        index_queue = collections.deque()
        
        for idx,val in enumerate(nums):
            index_queue.append(idx)
            while valdec_queue and valdec_queue[-1] < val:
                valdec_queue.pop()
            valdec_queue.append(val)
            
            if len(index_queue) == k:
                answ.append(valdec_queue[0])
                
                cur = index_queue.popleft()
                if nums[cur] == valdec_queue[0]:
                    valdec_queue.popleft()
                    
        return answ
            
            
# l = r = 0
        
#         while r < len(nums):
#             while dec_queue and nums[dec_queue[-1]] < nums[r]:
#                 dec_queue.pop()
                
#             dec_queue.append(r)
            
#             # remove left val from window
#             if l > dec_queue[0]:
#                 dec_queue.popleft()
                
#             if (r + 1) >= k:
#                 answ.append(nums[dec_queue[0]])
#                 l += 1
#             r += 1
            
#         return answ
        
        