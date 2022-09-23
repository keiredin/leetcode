class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answ = [0] * num_people
        i = 1
        j = 1
        while candies > 0:
            i = j % num_people
            answ[i-1] += min(j,candies)
            candies -= min(j,candies)
            j += 1
        return answ
                
            
        