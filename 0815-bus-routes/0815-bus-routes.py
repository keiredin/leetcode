class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0  
        
        n = len(routes)
        rmap = [[0] * n for _ in range(n)]      
        start, end = set(), set()  
        
        for i, route in enumerate(routes):      
            routes[i] = set(route)              
            if source in routes[i]:             
                start.add(i)
            if target in routes[i]:          
                end.add(i)
            if start and start & end:           
                return 1        
            
        if not start or not end: return -1      
        for i in range(n-1):
            for j in range(i+1, n):             
                if routes[i] & routes[j]:       
                    rmap[i][j] = rmap[j][i] = 1 

        q = deque([s for s in start])         
        visited = Counter(start)                  
        while q:
            cur = q.popleft()
            cnt = visited[cur]
            if cur in end:                      
                return cnt
            for i in range(n):                  
                if rmap[cur][i] and i not in visited:
                    q.append(i)
                    visited[i] = cnt + 1          
        return -1 

