class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([("0000", 0)])
        seen = {"0000"}
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        while queue:
            node,steps = queue.popleft()
            
            if node == target:
                return steps
            
           
            for i in range(0,len(node)):
                # add 1
                rightNeighbor = self.neighbor(node, i, 'right')
                # rotate left
                leftNeighbor = self.neighbor(node, i, 'left')
                
                if rightNeighbor not in seen and rightNeighbor not in deadends:
                    seen.add(rightNeighbor)
                    queue.append((rightNeighbor, steps+1))
                    
                if leftNeighbor not in seen and leftNeighbor not in deadends:
                    seen.add(leftNeighbor)
                    queue.append((leftNeighbor, steps+1))

        return -1
    
    def neighbor(self, node, curIdx, direction):
        if direction == 'right':
            if node[curIdx] != "9":
                neighbor = node[:curIdx] + str(int(node[curIdx]) + 1) + node[curIdx+1:]
            else:
                neighbor = node[:curIdx] + "0" + node[curIdx+1:]
                
        else:
            if node[curIdx] != "0":
                neighbor = node[:curIdx] + str(int(node[curIdx]) - 1) + node[curIdx+1:]
            else:
                neighbor = node[:curIdx] + "9" + node[curIdx+1:]
                
        return neighbor
                    
        