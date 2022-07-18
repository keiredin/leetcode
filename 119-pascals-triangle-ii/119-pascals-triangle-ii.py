class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answ = [[1]]
        
        for i in range(rowIndex):
            temp = [0] + answ[-1] + [0]
            curRow = []
            
            for j in range(len(answ[-1])+1):
                curRow.append(temp[j] + temp[j+1])
            
            answ.append(curRow)
        
        return answ[rowIndex] 
        