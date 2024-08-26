# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.helper(root, root.val)
        
    def helper(self, root, x):

        if root == None:
            return 0
        
        if root.val >= x:
            return 1 + self.helper(root.left, max(x, root.val)) + self.helper(root.right, max(x, root.val))
        
        else:
            return 0 + self.helper(root.left, max(x, root.val)) + self.helper(root.right, max(x, root.val))
        