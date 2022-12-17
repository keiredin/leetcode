class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        o = "+-/*"
        for i in tokens:
            if i in o: 
                num1 = s.pop()
                num2 = s.pop()
                if i == '+':
                    num2 += num1 
                    s.append(num2)
                elif i == '-':
                    num2 -= num1
                    s.append(num2)
                    
                elif i == '*':
                    num2 *= num1
                    s.append(num2)
                    
                elif i == '/':
                    if (num2 * num1 > 0):
                        num2 = num2 // num1
                    else:
                        num2 = (num2+(-num2 % num1)) //num1  
                    s.append(num2)
            else:
                s.append(int(i))
                
                    
        return s.pop()