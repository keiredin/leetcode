class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0 for _ in range(numCourses)]
        outDegree = defaultdict(set)
        
        for course, pre in prerequisites:
            outDegree[pre].add(course)
            inDegrees[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)
        
        answ = []
        while queue:
            course = queue.popleft()
            answ.append(course)
            for neighbor in outDegree[course]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor]==0:
                    queue.append(neighbor)
                    
        return answ if len(answ) == numCourses else []
        