# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = chr(ord('a') + 26) # create a STR_MAX

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node: Optional[TreeNode], cur_str: str):
            if not node: return
            cur_str = chr(ord('a') + node.val) + cur_str
            if not node.left and not node.right: # reached leaf node
                if cur_str < self.res: self.res = cur_str
            else:
                if node.left:
                    dfs(node.left, cur_str)
                if node.right:
                    dfs(node.right, cur_str)
                    
        dfs(root, "")

        return self.res
        