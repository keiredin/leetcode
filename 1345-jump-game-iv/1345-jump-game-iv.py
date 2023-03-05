class Solution:
    def minJumps(self, arr: List[int]) -> int:
        valIndexPair = dict()
        for i in range(len(arr)):
            if arr[i] not in valIndexPair:
                valIndexPair[arr[i]] = [i]
            else:
                valIndexPair[arr[i]].append(i)     
                
        q = deque()
        inbound = lambda i: 0 <= i < len(arr)
        visited = set()
        q.append((0,0))
        while q:
            curr,move = q.popleft()
            visited.add(curr)
            if curr == len(arr) - 1:
                return move
            
            left = curr -1
            right = curr + 1
            equal = valIndexPair[arr[curr]]
            
            if inbound(left) and left not in visited:
                q.append((left,move+1))
            if inbound(right) and right not in visited:
                q.append((right,move+1))
            for i in equal:
                if inbound(i) and i not in visited:
                        q.append((i,move+1))
                        
            valIndexPair[arr[curr]] = []
            
            

                
            
                
            