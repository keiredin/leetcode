class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i] >= 9:
                digits[i] = 0
                remainder = 1
            else:
                digits[i] += 1
                remainder = 0
                break
        return digits if not remainder else [1] + digits
                
        