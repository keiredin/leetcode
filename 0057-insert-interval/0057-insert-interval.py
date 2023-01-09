class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        
        answer = [intervals[0]]
        prev_end = intervals[0][1]
        
        for start,end in intervals[1:]:
            if start > prev_end:
                answer.append([start,end])
                prev_end = end
            else:
                prev_end = max(prev_end,end)
                answer[-1][1] = prev_end
                
        return answer
        