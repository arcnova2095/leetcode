# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t :
            return True
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def isSameTree(self,s,t):
        if not s and not t:
            return True
        return self.isSameTree(s.right,t.right) and self.isSameTree(s.left,t.left) if s and t and s.val==t.val else False
        