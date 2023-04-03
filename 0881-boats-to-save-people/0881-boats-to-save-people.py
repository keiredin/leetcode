class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boat = 0
       
        while left <= right:
            if people[left] + people[right] > limit:
                boat += 1
                right -= 1
            else:
                left += 1
                right -= 1
                boat += 1
        return boat
                
            
            
            
        