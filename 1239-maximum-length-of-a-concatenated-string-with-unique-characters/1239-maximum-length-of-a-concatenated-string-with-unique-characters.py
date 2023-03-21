class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        def backtrack(i,path):
            nonlocal res
            if len(set(path)) == len(path):
                res = max(res, len(path))
                
            for j in range(i,len(arr)):
                backtrack(j+1, path+arr[j])
                
        backtrack(0,"")
        return res
        