class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        dec_stack = []
        
        for idx, val in enumerate(height):
            if not dec_stack:
                dec_stack.append(idx)
            else:
                while dec_stack and height[dec_stack[-1]] < val:
                    pop = dec_stack.pop()
                    if not dec_stack:
                        break
                    
                    h = min(height[dec_stack[-1]], val) - height[pop]
                    width = idx - dec_stack[-1] - 1
                    
                    res += h * width
                        
                dec_stack.append(idx)
                
        return res
            
        
        