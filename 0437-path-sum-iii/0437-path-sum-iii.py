# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        hashmap = {0: 1}
        
        
        def dfs(root, target_sum, current_sum, hashmap):
            if not root:
                return 0
            current_sum += root.val
            count = hashmap.get(current_sum - target_sum, 0)
            hashmap[current_sum] = hashmap.get(current_sum, 0) + 1
            count += dfs(root.left, target_sum, current_sum, hashmap)
            count += dfs(root.right, target_sum, current_sum, hashmap)
            hashmap[current_sum] -= 1
            return count
        
        return dfs(root, targetSum, 0, hashmap)