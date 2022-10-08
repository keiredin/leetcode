class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answ = []
        def backtrack(i,lst,curSum):
            if curSum == target:
                answ.append(tuple(lst))
                return
            if curSum > target:
                return
                
            for j in range(i,len(candidates)):
                lst.append(candidates[j])
                backtrack(j,lst, curSum + candidates[j])
                lst.pop()
          
        backtrack(0,[],0)
        return answ
        