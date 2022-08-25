class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        orgK = k
        left,right = 0,0
        
        maxFs = 0
        while right < len(answerKey):
            if answerKey[right] == 'T' and k > 0:
                right += 1
                k -= 1
            elif answerKey[right] == 'T' and k == 0:
                maxFs = max(maxFs, right- left)
                if answerKey[left] == 'T':
                    k += 1
                left += 1
            else:
                right+= 1
                
        maxFs = max(maxFs, right- left)
        
        
        left,right,k = 0,0,orgK
        maxTs = 0
        while right < len(answerKey):
            if answerKey[right] == 'F' and k > 0:
                right += 1
                k -= 1
            elif answerKey[right] == 'F' and k == 0:
                maxTs = max(maxTs, right- left)
                if answerKey[left] == 'F':
                    k += 1
                left += 1
            else:
                right+= 1
                
        maxTs = max(maxTs, right- left)
        
        return max(maxFs,maxTs)