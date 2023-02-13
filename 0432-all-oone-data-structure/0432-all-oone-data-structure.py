class AllOne:
    def __init__(self):
        self.Count = defaultdict(int)

    def inc(self, key: str) -> None:
        self.Count[key] += 1        

    def dec(self, key: str) -> None:
        if self.Count[key] > 1:
            self.Count[key] -= 1
        else:
            del self.Count[key]        

    def getMaxKey(self) -> str:
        ans = ""
        maxCount = 0
        for key, value in self.Count.items():
            if value > maxCount:
                ans = key
                maxCount = value
        return ans 

    def getMinKey(self) -> str:
        ans = ""
        minCount = float('inf')
        for key, value in self.Count.items():
            if value < minCount:
                ans = key
                minCount = value
        return ans        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()