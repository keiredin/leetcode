class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if len(word) >= len(pref):
                count += word[:len(pref)] == pref
        return count