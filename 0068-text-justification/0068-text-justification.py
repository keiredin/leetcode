class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            if len(w) > maxWidth:
                print("wwwwwwwwwwwwwww")
                return ""
            
            # Check if the word can be added in the cur line
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
            
        return res + [' '.join(cur).ljust(maxWidth)]