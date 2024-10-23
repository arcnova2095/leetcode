# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q= deque()
        if root:
            q.append((root.val,root))
        while q:
            n= len(q)
            levelSum=0
            for val,node in q:
                levelSum+=node.val
            for i in range(n):
                val,node=q.popleft()
                childSum=0
                if node.left: childSum += node.left.val
                if node.right: childSum += node.right.val

                if node.left: q.append((childSum, node.left))
                if node.right: q.append((childSum, node.right))

                node.val= levelSum-val
        return root