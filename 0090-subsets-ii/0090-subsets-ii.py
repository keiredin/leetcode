class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        ans = []
        self.backTrack(0, [],ans, nums)
        
        return ans
    
    def backTrack(self,start, cur_list,ans, nums):
            ans.append(cur_list[:])
            
            prev = -11
            for j in range(start, len(nums)):
                if nums[j] != prev:
                    cur_list.append(nums[j])
                    self.backTrack(j+1, cur_list, ans, nums)
                    cur_list.pop()
                    prev = nums[j]
                    
                
             