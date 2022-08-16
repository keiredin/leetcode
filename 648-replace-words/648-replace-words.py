class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end=True

    def search(self, word: str) -> bool:
        cur = self.root
        answ = ""
        for char in word:
            if cur.end == True:
                return answ
            if char not in cur.children:
                return ""
            answ += char
            cur = cur.children[char]
        return ""

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
    
    

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        res = ""
        for root in dictionary:
            trie.insert(root)
            
        sentence = sentence.split()
        for word in sentence:
            rootWord = trie.search(word)
            if rootWord:
                res += rootWord
            else:
                res += word
            res += " "
        
        return res.strip()
        
                
            
            
        