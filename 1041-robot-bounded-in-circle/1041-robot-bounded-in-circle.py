class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        curDirection = [0,1]    #north    

        for op in instructions:
            if op == "G":
                new_x, new_y = curDirection
                x, y = x + new_x, y + new_y
            
            elif op == "R":
                old_x,old_y = curDirection
                curDirection = [old_y, old_x * -1]
            else:
                old_x,old_y = curDirection
                curDirection = [-1 * old_y, old_x]

        return curDirection != [0,1] or (x == 0 and y == 0)