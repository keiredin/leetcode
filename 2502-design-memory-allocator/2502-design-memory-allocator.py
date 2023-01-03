class Allocator:

    def __init__(self, n: int):
        self.memory = [-1] * n
        self.allocatedIndex = defaultdict(list)
        

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(len(self.memory)):
            if self.memory[i] == -1: 
                cnt += 1
            else:
                cnt = 0
                
            if cnt == size:
                self.memory[i+1-cnt:i+1] = [mID] * cnt
                self.allocatedIndex[mID].extend(list(range(i+1-cnt,i+1)))
                return i+1-cnt
            
        return -1
        

    def free(self, mID: int) -> int:
        freedBlock = len(self.allocatedIndex[mID])
        for idx in self.allocatedIndex[mID]:
            self.memory[idx] = -1
            
        self.allocatedIndex[mID] = []
        
        return freedBlock
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)