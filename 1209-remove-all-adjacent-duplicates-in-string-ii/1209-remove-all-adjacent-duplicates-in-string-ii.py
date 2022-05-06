class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
            if not stack:
                stack.append((i,1))
            else:
                top,count = stack[-1]
                if i == top:
                    if count == k-1:
                        del stack[-count:]    # or len(stack)-top[1]: - to remove the last n element lst[-n:]
                    else:
                        stack.append((i,count+1))
                else:
                    stack.append((i,1))
        return "".join(i[0] for i in stack)
            
        