# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find(root, maxVal):
            res=0
            if not root:
                return 0
            if root.val>=maxVal:
                res=1
            
            maxVal= max(maxVal,root.val)
            res+= find(root.left,maxVal)
            res+= find(root.right,maxVal)

            return res

        return find(root,root.val)