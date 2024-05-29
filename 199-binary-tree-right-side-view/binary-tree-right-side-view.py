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
                val=[]
                for i in range(len(q)):
                    r= q.popleft()
                    val.append(r.val)
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                res.append(val)
            ans=[]
            for i in res:
                ans.append(i[-1])
            return ans
        