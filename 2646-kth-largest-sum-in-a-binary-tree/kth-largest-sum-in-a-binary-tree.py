# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q= collections.deque()
        m= []
        if root:
            q.append(root)
        while q:
            s= 0
            for i in range(len(q)):
                p= q.popleft()
                s+=p.val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            m.append(s)
        m.sort()
        return m[-k] if k<=len(m) else -1