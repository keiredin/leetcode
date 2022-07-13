class Solution:
		def makesquare(self, matchsticks: List[int]) -> bool:
			total = sum(matchsticks)
			if total % 4:
				return False
			target = total >> 2
			nums = []
			for n in matchsticks:
				if n > target:
					return False
				elif n < target:
					nums.append(n)

			if nums == []:
				return True
			k = 4 - (len(matchsticks) - len(nums))
			nums.sort(reverse=True)
			used = [False] * len(nums)

			def helper(nums, used, start, target, sum, k):
				if k == 1:
					return True

				i = start
				while i < len(nums):
					if not used[i]:
						used[i] = True
						if sum + nums[i] < target and helper(nums, used, i + 1, target, sum + nums[i], k):
							return True
						if sum + nums[i] == target and helper(nums, used, 0, target, 0, k - 1):
							return True
						used[i] = False
						while i + 1 < len(nums) and nums[i + 1] == nums[i]:
							i += 1
						if sum == 0:
							return False
					i += 1
				return False

			return helper(nums, used, 0, target, 0, k)







# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         n = len(matchsticks)
        
#         # We don't even have 4 matchsticks to form a square
#         if n < 4:
#             return False
    
#         matchsticks_sum = sum(matchsticks)
        
#         # Can't divide into 4 equal sides
#         if matchsticks_sum % 4 != 0:
#             return False
        
#         # The size of each side
#         side = matchsticks_sum // 4
        
#         # Simulate the square. We will fill the sies in the DFS
#         square_sides = [0,0,0,0]
        
#         # Sort to optimize the DFS by exiting early because we will start with the biggest elements
#         matchsticks.sort(reverse=True)
        
#         def dfs(i):
#             if i == n:
#                 side_a = square_sides[0]
#                 side_b = square_sides[1] 
#                 side_c = square_sides[2] 
#                 side_d = square_sides[3] 
                
#                 # Return true only if all sides are equal to the "side" size we are looking for
#                 return side == side_a == side_b == side_c == side_d
        
#             for side_i in range(4):
                
#                 if square_sides[side_i] + matchsticks[i] > side:
#                     continue
                    
#                 # Add the matchstick size to the side of the box
#                 square_sides[side_i] += matchsticks[i]
                
#                 if dfs(i + 1):
#                     return True
                
#                 # Backtrack if we didn't find the answer
#                 square_sides[side_i] -= matchsticks[i]
            
#             return False
        
        
#         return dfs(0)


# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         targetLength = sum(matchsticks) // 4
#         sides = [0] * 4
        
#         if sum(matchsticks) / 4 != targetLength:
#             return False
        
#         matchsticks.sort(reverse=True)  # just to maximize the alg. speed
        
#         def backtrack(i):
#             if i == len(matchsticks):
#                 return True
            
#             for j in range(4):
#                 if sides[j] + matchsticks[i] <= targetLength:
#                     sides[j] += matchsticks[i]
#                     if backtrack(i + 1):
#                         return True
                    
#                     sides[j] -= matchsticks[i]  # else reverse the desicion we've just made
#             return False
        
#         return backtrack(0)
        
        