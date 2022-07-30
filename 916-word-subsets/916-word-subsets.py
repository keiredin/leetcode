class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        char_freq = defaultdict(int)
        
        for w2 in words2:
            cnt = Counter(w2)
            for char in cnt:
                if char in char_freq:
                    char_freq[char] = max(char_freq[char], cnt[char])
                else:
                    char_freq[char] = cnt[char]
        answ = []            
        for w1 in words1:
            count_char = Counter(w1)
            flag = True
            for key in char_freq:
                if key not in count_char or count_char[key] < char_freq[key]:
                    flag = False
                    break
            if flag:
                answ.append(w1)
        
        return answ
        
                    
            
        