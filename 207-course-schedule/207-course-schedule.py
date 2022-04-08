class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees = [0 for _ in range(numCourses)]
        outDegree = defaultdict(set)
        
        for course, pre in prerequisites:
            outDegree[pre].add(course)
            inDegrees[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in outDegree[course]:
                inDegrees[neighbor]-=1
                if inDegrees[neighbor]==0:
                    queue.append(neighbor)
                    
        return count==numCourses

        




# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#         '''
#         solution approach:
#         1. create the adjacency list from given edges
#         2. for each node, traverse graph starting at this node (BFS/DFS); 
#             if we detect a loop, return False
#         3. return True
#         '''
        
#         # create adjacency list
#         graph = [[] for _ in range(numCourses)]
#         print(graph)
#         for a,b in prerequisites:
#             graph[a].append(b)
#             #graph[b].append(a)  # no, because graph is directional!
                                 
#         for n in range(0,numCourses):
#             Q = deque(graph[n])
#             visited = set()
#             while Q:
#                 m = Q.popleft()  # --> BFS
#                 #m = Q.pop()     # --> DFS
#                 if m==n:
#                     # we detected a loop
#                     return False
#                 visited.add(m)  # this is just for optimization, not strictly needed
#                 for neighbor in graph[m]:
#                     if neighbor not in visited:
#                         Q.append(neighbor)
        
#         return Truerint(graph)
