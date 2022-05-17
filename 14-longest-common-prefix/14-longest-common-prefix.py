class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = zip(*strs)
        answ = ""
        for i in list(f):
            if i.count(i[0]) != len(i):
                return answ
            answ += i[0]
        return answ
        