class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def setIsWord(self):
        self.isWord = True
        
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

                          
                            
class Solution:
    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        repetition = defaultdict(int)
        trie = Trie()
        for word in words:
            if not trie.search(word):
                trie.insert(word)
            repetition[word] += 1
        
        print(repetition.items())
        new = sorted(repetition.items(), key = lambda x: (-1*x[1], x[0]))
        print(new)
        answer = []
        for i in range(k):
            answer.append(new[i][0])
        return answer
        
    
    
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         trie = Trie()
#         count = {}
        
#         for word in words:
#             if trie.search(word) == False:
#                 count[word] = 1
#                 trie.insert(word)
#             else:
#                 count[word] += 1
        
#         sort_count = sorted(count.items(), key = lambda x: (-1*x[1], x[0])) # sort the count dict by val - rev

#         answ = []
#         for i in range(k):
#             answ.append(sort_count[i][0])
        
#         return answ