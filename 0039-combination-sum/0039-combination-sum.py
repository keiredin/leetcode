class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answ = []
        def backtrack(i,lst,targetSum):
            if i == len(candidates):
                if targetSum == 0:
                    answ.append(tuple(lst))
                return
            
            if candidates[i] <= targetSum:
                lst.append(candidates[i])
                backtrack(i,lst, targetSum - candidates[i])
                lst.pop()
                
            backtrack(i + 1,lst, targetSum)
          
        backtrack(0,[],target)
        return answ
        