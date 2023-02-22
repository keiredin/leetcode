class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        seconds_needed = 0
        temp = []
        while True:
            i = 0
            process_complete = True
            while i < len(s):
                if i < len(s)-1 and s[i] == '0'and s[i+1] == '1':
                    temp.append('1')
                    temp.append('0')
                    i += 2
                    process_complete = False
                else:                        
                    temp.append(s[i])
                    i += 1
                                
            s = "".join(temp)
            temp = []
                    
            if process_complete:
                break
                
            seconds_needed += 1
        return seconds_needed
            