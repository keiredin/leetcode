class Solution:
    def minOperations(self, logs: List[str]) -> int:
        specialChar = {"./", "../"}
        stack = []
        
        for log in logs:
            if log in specialChar:
                if stack and log == "../":
                    stack.pop()
            else:
                stack.append(log)
                
        return len(stack)
        