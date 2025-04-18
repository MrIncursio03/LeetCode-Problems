# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return 0, None
            d1, lca1 = helper(root.left)
            d2, lca2 = helper(root.right)
            if d1 > d2:
                node = lca1
            elif d1 < d2:
                node = lca2
            else:
                node = root
            return max(d1, d2) + 1, node
        return helper(root)[1]
