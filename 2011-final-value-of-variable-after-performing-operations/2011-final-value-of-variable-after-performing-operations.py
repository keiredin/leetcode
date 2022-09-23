class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answ = 0
        for op in operations:
            if op == '++X' or op == 'X++':
                answ += 1
            else:
                answ -= 1
        return answ
        