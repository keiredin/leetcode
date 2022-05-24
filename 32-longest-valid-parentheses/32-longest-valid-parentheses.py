# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         max_length = 0
#         stck=[-1] # initialize with a start index
#         for i in range(len(s)):
#             if s[i] == '(':
#                 stck.append(i)
#             else:
#                 stck.pop()
#                 if not stck: # if popped -1, add a new start index
#                     stck.append(i)
#                 else:
#                     max_length=max(max_length, i-stck[-1]) # update the length of the valid substring
#         return max_length
                
            
            
 # time O(n) and space O(1)          
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left,right,maxLength = 0,0,0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif right >= left:
                left = right = 0

        left = right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif left >= right:
                left = right = 0
    
        return maxLength