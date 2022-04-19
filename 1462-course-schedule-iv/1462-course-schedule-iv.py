class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        inDegrees = [0 for _ in range(numCourses)]
        outDegree = defaultdict(set)
        pre_lookup = defaultdict(set)  # store the prerequisites info for each node
    
        
        for pre, course in prerequisites:
            outDegree[pre].add(course)
            inDegrees[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)
        
        # topo_order = []
        while queue:
            curr = queue.popleft()
            # topo_order.append(course)
            for neighbor in outDegree[curr]:
                pre_lookup[neighbor].add(curr)   # add current node as the prerequisite of this neighbor node
                pre_lookup[neighbor].update(pre_lookup[curr])  # add all the preqs for current node to the neighbor node's preqs
                
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor]==0:
                    queue.append(neighbor)
        
        
        # traverse the queries and return the results
        answ = [True if q[0] in pre_lookup[q[1]] else False for q in queries]
        return answ
        