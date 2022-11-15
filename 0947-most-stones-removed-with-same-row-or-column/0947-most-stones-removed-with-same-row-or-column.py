class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for stone in stones:
            graph[tuple(stone)] = []
        
        for stone in stones:
            x,y = stone
            for key in graph:
                if (x == key[0] or y == key[1]) and list(key) != stone:
                    graph[key].append(stone)
                    
        def dfs(curPoint):
            visited.add(tuple(curPoint))
            for neighbor in graph[tuple(curPoint)]:
                if tuple(neighbor) not in visited:
                    dfs(tuple(neighbor))
            return
        
        visited = set()
        count = 0
        for stone in stones:
            if tuple(stone) not in visited:
                count += 1 
                dfs(tuple(stone))
        
        # print(visited)
        return len(stones) - count
     
            
            