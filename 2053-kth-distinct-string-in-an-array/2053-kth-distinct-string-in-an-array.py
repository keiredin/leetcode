class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        for char in count:
            if count[char] == 1:
                k -= 1
            if k == 0:
                return char
        return ""
        