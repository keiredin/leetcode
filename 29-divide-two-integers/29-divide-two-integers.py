class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        if dividend < 0 :
            dividend = dividend - dividend - dividend
        if divisor < 0:
            divisor = divisor - divisor - divisor
            
        if divisor == 1 :
            return self.handleResult(sign * dividend)
       
        result = 0
        while dividend >= divisor:
            toSubstract, quotient = self.computeIteration(dividend, divisor)
            dividend -= toSubstract
            result += quotient

        
        return self.handleResult(sign * result)
    
    def handleResult(self, result):
        if result < pow(-2, 31):
            return pow(-2, 31)
        if result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        return result
    
    def computeIteration(self, dividend, divisor):
        dividendStr = str(dividend)
        divisorStr = str(divisor)
        numberOfZeros = len(dividendStr) - len(divisorStr)
        if int(dividendStr[0:len(divisorStr)]) < divisor:
            numberOfZeros -= 1
        return int(divisorStr + '0' * numberOfZeros), int('1' + '0' * numberOfZeros)