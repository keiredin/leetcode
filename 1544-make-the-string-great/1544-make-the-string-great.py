class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and ord(char) < 97 and ord(stack[-1]) - ord(char) == 32:
                stack.pop()
            elif stack and ord(char) >= 97 and ord(char) - ord(stack[-1])  == 32:
                stack.pop()
            else:
                stack.append(char)
                
        return "".join(stack)
        