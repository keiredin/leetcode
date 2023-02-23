class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # base case
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i in range(len(expression)):
            # split input at each operator
            if expression[i] in "+-*":
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                for x in left_results:
                    for y in right_results:
                        if expression[i] == "+":
                            res.append(x+y)
                        elif expression[i] == "-":
                            res.append(x-y)
                        elif expression[i] == "*":
                            res.append(x*y)
        return res
        
