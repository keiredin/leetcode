class RandomizedCollection:

    def __init__(self):
        self.numsCount = defaultdict(int)
        self.numsIndex = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        temp = self.numsCount[val] == 0
        self.numsCount[val] += 1
        self.nums.append(val)
        self.numsIndex[val].add(len(self.nums)-1)
        
        return temp
          

    def remove(self, val: int) -> bool:
        if self.numsCount[val] == 0:
            return False
        
        self.numsCount[val] -= 1
        
        if self.nums[-1] == val:
            self.nums.pop()
            self.numsIndex[val].remove(len(self.nums))
        
        else:
            index = self.numsIndex[val].pop()
            
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.nums.pop()
            
            self.numsIndex[self.nums[index]].add(index)
            self.numsIndex[self.nums[index]].remove(len(self.nums))
            
            
            
        return True
            
        
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums)-1)
        
        return self.nums[index]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()