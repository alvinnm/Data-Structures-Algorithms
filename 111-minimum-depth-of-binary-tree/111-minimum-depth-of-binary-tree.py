# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans =  1
        q = [root]
        if not root: return 0
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if not node.left and not node.right:
                    return ans
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += 1
        return 