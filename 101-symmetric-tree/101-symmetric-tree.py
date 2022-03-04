# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(L, R):
            if L and R:
                return L.val == R.val and check(L.left, R.right) and check(L.right, R.left)
            return L == R
        if not root:
            return True
        return check(root.left, root.right)
        
                