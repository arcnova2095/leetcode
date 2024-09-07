# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
            res=[]
            q= deque()
            if root:
                q.append(root)
            while q:
                sub=[]
                for i in range(len(q)):
                    x=q.popleft()
                    sub.append(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
                res.append(sub[:])
            return res



