class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dec_stack = []
        answer = [0] * len(temperatures)
        
        for i,num in enumerate(temperatures):
            while dec_stack and temperatures[dec_stack[-1]] < num:
                idx = dec_stack.pop()
                answer[idx] = i - idx
                
            dec_stack.append(i)
            
        return answer
        