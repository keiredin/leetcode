class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            
            for neighbor in rooms[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
        return len(visited) == len(rooms)
            
        