class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answ = []     
        self.generatePermutation(0,nums,answ)
        return answ
        
    def generatePermutation(self,idx,nums,answ):
        if idx >= len(nums):
            answ.append(nums.copy())
        
        for i in range(idx, len(nums)):
            self.swap(i,idx,nums)
            self.generatePermutation(idx+1, nums, answ)
            self.swap(i,idx,nums)
        
    def swap(self,i,j,nums):
        nums[i],nums[j] = nums[j], nums[i]

        
        
#        # using visited 
#         answ = []
#         pickedIndex = defaultdict()
        
#         # initialize all index as not picked up
#         for i in range(len(nums)):
#             pickedIndex[i] = False
            
#         self.recurPerm(0,[],pickedIndex,nums,answ)
        
#         return answ
    
    
#     def recurPerm(self,i, curList, picked, nums, answ):
#         if len(curList) == len(nums):
#             answ.append(curList.copy())
            
#         for j in range(len(nums)):
#             if picked[j] == False:
#                 picked[j] = True
#                 curList.append(nums[j])
#                 self.recurPerm(j, curList, picked, nums, answ)
#                 picked[j] = False
#                 curList.pop()
        
# Time = n! * n(n for deep copy of the array)
# space = 2n - for map and curList
