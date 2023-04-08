# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))
    
    def construct(self, nums: List[int], l: int, r: int) -> TreeNode:
        if l == r:
            return None
        max_i = self.max(nums, l, r)
        root = TreeNode(nums[max_i])
        root.left = self.construct(nums, l, max_i)
        root.right = self.construct(nums, max_i + 1, r)
        return root
    
    def max(self, nums: List[int], l: int, r: int) -> int:
        max_i = l
        for i in range(l, r):
            if nums[max_i] < nums[i]:
                max_i = i
        return max_i
    
        