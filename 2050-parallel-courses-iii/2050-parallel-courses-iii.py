class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        inDegrees = [0 for _ in range(n)]
        outDegree = defaultdict(set)
        
        for pre, course in relations:
            outDegree[pre].add(course)
            inDegrees[course-1] += 1
        
        queue = deque()
        for i in range(n):
            if inDegrees[i]==0:
                queue.append(i+1)
                
        shortest_time = time[:]
        while queue:
            course = queue.popleft()
            
            for neighbor in outDegree[course]:
                shortest_time[neighbor-1] = max(shortest_time[neighbor-1], shortest_time[course-1]+time[neighbor-1])
                inDegrees[neighbor-1] -= 1
                if inDegrees[neighbor-1]==0:
                    queue.append(neighbor)
                    
        return max(shortest_time)














# class Solution:
#     def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
#         inDegrees = [0 for _ in range(n)]
#         outDegree = defaultdict(set)
        
#         for pre, course in relations:
#             outDegree[pre].add(course)
#             inDegrees[course-1] += 1
        
#         queue = deque()
#         for i in range(n):
#             if inDegrees[i]== 0:
#                 queue.append(i+1)
        
        
#         total_time = 0
#         maxx = -inf
#         while queue:
#             course = queue.popleft()
#             maxx = max(maxx,time[course-1])
            
#             if len(queue) == 0:
#                 total_time += maxx
#                 maxx = -inf
            
#             for neighbor in outDegree[course]:
#                 inDegrees[neighbor-1] -= 1
#                 if inDegrees[neighbor-1]==0:
#                     total_time += maxx if maxx > time[neighbor-1] else 0
#                     maxx -= time[course-1]
#                     queue.append(neighbor)
        
#         return total_time