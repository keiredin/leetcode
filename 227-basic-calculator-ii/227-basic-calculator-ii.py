class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack, curr, opr = [], 0, "+"
        operators = {"+", "-" , "*" ,"/"}
        nums = set(str(n) for n in range(10))

        for indx in range(len(s)):
            char = s[indx]

            if char in nums:
                curr = curr * 10 + int(char)
            if char in operators or indx == len(s) - 1:
                if opr == "+":
                    stack.append(curr)
                elif opr == "-":
                    stack.append(-curr)
                elif opr == "*":
                    stack[-1] *= curr
                elif opr == "/":
                    stack[-1] = int(stack[-1] / curr)

                curr = 0
                opr = char
            
        return sum(stack)
        
            
        