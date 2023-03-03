class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle.strip()
        return haystack.find(needle,0,len(haystack)) if len(needle) > 0 else 0