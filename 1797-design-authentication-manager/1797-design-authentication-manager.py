class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.hashMap = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hashMap[tokenId] = currentTime + self.timeToLive
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hashMap:
            if currentTime < self.hashMap[tokenId]:
                self.hashMap[tokenId] = currentTime + self.timeToLive
            

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for k,v in self.hashMap.items():
            if v > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)