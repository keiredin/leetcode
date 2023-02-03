class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [""] * numRows
        numRows -= 1
        for x in range(len(s)):
            zigzag[abs((x + numRows) % (2 * numRows) - numRows)] += s[x]
        return "".join(zigzag)
    
    
    
    
# The absolute value function takes the x value and creates a pattern that goes from 0 to numRows - 1 and back down (e.g. 0 1 2 3 2 1 0 1 2 3). This just targets the correct row to add the next character into. numRows is decremented in order to make the function have the correct amount of indexes.
        