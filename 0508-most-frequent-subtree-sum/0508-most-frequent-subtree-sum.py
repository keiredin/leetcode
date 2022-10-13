# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_freq = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            curSubtreeSum = left + right + node.val
            sum_freq[curSubtreeSum] += 1
            
            return curSubtreeSum
        dfs(root)
        
        maxFrequent = max(sum_freq.values())
        answ = []
        for summ in sum_freq:
            if sum_freq[summ] == maxFrequent:
                answ.append(summ)
                
        return answ