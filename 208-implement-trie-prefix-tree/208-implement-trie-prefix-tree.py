class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                cur.children[c] = Node()
            cur = cur.children[c]   
        cur.isWord = True
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                return False
            cur = cur.children[c]
        return cur.isWord 

    def startsWith(self, prefix: str) -> bool:
            cur = self.root
            for c in prefix:
                if not cur.children.get(c):
                    return False
                cur = cur.children[c]  
            return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)