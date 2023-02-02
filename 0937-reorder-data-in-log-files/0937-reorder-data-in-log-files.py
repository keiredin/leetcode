class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs,digitLogs = [],[]
        
        for log in logs:
            if (log.split()[1]).isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log.split())
                
        
                
        letterLogs.sort(key = lambda x: x[0])
        letterLogs.sort(key = lambda x: x[1:])
        
        for i in range(len(letterLogs)):
            letterLogs[i] = " ".join(letterLogs[i])
            
        letterLogs.extend(digitLogs)
        return letterLogs
        