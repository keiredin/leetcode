class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        i,j = 0,0
        while i<len(matrix):
            if(target == matrix[i][len(matrix[0])-1]):
                return 1
            elif(target > matrix[i][len(matrix[0])-1]):
                i+=1
                continue
            else:
                low = 0
                high = len(matrix[0])-1
                while low<=high:
                    mid = (low+high)//2
                    if(matrix[i][mid] == target):
                        return 1
                    elif(matrix[i][mid]>target):
                        high-=1
                    else:
                        low+=1
            i+=1
        return 0