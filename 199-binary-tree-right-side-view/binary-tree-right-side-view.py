# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            
            res=[]
            q= deque()
            if root:
                q.append(root)
            while q:
                sub=[]
                for i in range(len(q)):
                    node= q.popleft()
                    sub.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(sub)
            r=[]
            for i in res:
                r.append(i[-1])
            return r
        