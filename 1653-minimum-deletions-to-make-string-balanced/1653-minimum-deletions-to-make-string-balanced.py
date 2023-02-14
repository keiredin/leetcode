class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        deletions = 0
        
        for char in s:
            if stack and char == "a":
                stack.pop()
                deletions += 1
            elif char == "b":
                stack.append(char)
                
        return deletions
                