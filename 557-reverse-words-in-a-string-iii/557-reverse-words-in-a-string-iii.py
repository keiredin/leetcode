class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(substr[::-1] for substr in s.split())
        