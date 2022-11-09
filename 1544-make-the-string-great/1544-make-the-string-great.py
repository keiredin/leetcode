class Solution:
    def makeGood(self, s: str) -> str:
#         stack = []
        
#         for char in s:
#             if stack and abs(ord(stack[-1]) - ord(char)) == 32:
#                 stack.pop()
            
#             else:
#                 stack.append(char)
                
#         return "".join(stack)
        
        #two pointers approach
        s = list(s)
        end = 0 # points to the element after the good string
        
        for cur in range(len(s)):
            if end > 0 and abs(ord(s[cur]) - ord(s[end-1])) == 32:
                end -= 1
            else:
                s[end] = s[cur]
                end += 1
                
        return "".join(s[:end])
        