class Solution:
    def checkValidString(self, s: str) -> bool:
        openParenthesis = []
        stars = deque([])
        
        for i,char in enumerate(s):
            if char == ")":
                if openParenthesis:
                    openParenthesis.pop()
                elif stars:
                    stars.popleft()
                else:
                    return False
            elif char == "(":
                openParenthesis.append(i)
            else:
                stars.append(i)
     
        while openParenthesis and stars:
            if openParenthesis[-1] < stars[-1]:
                openParenthesis.pop()
                stars.pop()
            else:
                break
            
        return len(openParenthesis) == 0
        
        