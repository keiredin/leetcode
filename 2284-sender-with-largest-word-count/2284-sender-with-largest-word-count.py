class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sendersWordCount = defaultdict(int)
        
        for i in range(len(messages)):
            sender = senders[i]
            sendersWordCount[sender] += len(messages[i].split(" "))
            
        arr = [[v,k] for k,v in sendersWordCount.items()] # convert the dictionary to array
        
        arr.sort(key = lambda x : (x[0], x[1] ))
        
        return arr[-1][1]