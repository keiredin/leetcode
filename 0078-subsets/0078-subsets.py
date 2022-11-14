# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]
        
#         for num in nums:
#             output += [curr + [num] for curr in output]
        
#         return output

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(start, cur_list):
            if start == len(nums):
                ans.append(cur_list[:])
                return
            
            #pick
            cur_list.append(nums[start])
            backTrack(start+1, cur_list)
            
            
            #notPick
            cur_list.pop()
            backTrack(start+1, cur_list)

            # for j in range(start, n):
            #     cur_list.append(nums[j])
            #     backTrack(j+1, cur_list)
            #     cur_list.pop()

        n = len(nums)
        ans = []

        backTrack(0, [])

        return ans
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first = 0, curr = []):
#             # if the combination is done
#             if len(curr) == k:  
#                 output.append(curr[:])
#                 return
#             for i in range(first, n):
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
        
#         output = []
#         n = len(nums)
#         for k in range(n + 1):
#             backtrack()
#         return output
        