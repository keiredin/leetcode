class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        result = []
        for word in words:
            visited = [False] * len(word)
            if self.dfs(word, 0, visited, dictionary):
                result.append(word)
        return result
        
    def dfs(self, word: str, length: int, visited: List[bool], dictionary: set) -> bool:
        if length == len(word):
            return True
        if visited[length]:
            return False
        visited[length] = True
        for i in range(len(word) - (1 if length == 0 else 0), length, -1):
            if word[length:i] in dictionary and self.dfs(word, i, visited, dictionary):
                return True
        return False