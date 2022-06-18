#approach 1
# Trie = lambda: collections.defaultdict(Trie)
# WEIGHT = False

# class WordFilter(object):
#     def __init__(self, words):
#         self.trie1 = Trie() #prefix
#         self.trie2 = Trie() #suffix
#         for weight, word in enumerate(words):
#             cur = self.trie1
#             self.addw(cur, weight)
#             for letter in word:
#                 cur = cur[letter]
#                 self.addw(cur, weight)

#             cur = self.trie2
#             self.addw(cur, weight)
#             for letter in word[::-1]:
#                 cur = cur[letter]
#                 self.addw(cur, weight)

#     def addw(self, node, w):
#         if WEIGHT not in node:
#             node[WEIGHT] = {w}
#         else:
#             node[WEIGHT].add(w)

#     def f(self, prefix, suffix):
#         cur1 = self.trie1
#         for letter in prefix:
#             if letter not in cur1: return -1
#             cur1 = cur1[letter]

#         cur2 = self.trie2
#         for letter in suffix[::-1]:
#             if letter not in cur2: return -1
#             cur2 = cur2[letter]

#         return max(cur1[WEIGHT] & cur2[WEIGHT])


Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]