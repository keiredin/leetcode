class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        char = {'','.','..'}
        for s in path:
            if s in char:
                if stack and s == '..':
                    stack.pop()
            else:
                stack.append(s)
                
        answ = '/'.join(stack)
        return '/' + answ