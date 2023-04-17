class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        
        for i,val in enumerate(candies):
            if val + extraCandies >= maxx:
                candies[i] = True
            else:
                candies[i] = False
                
        return candies
        