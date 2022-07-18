class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answ = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + answ[-1] + [0]
            curRow = []
            
            for j in range(len(answ[-1])+1):
                curRow.append(temp[j] + temp[j+1])
            
            answ.append(curRow)
            
        return answ
        