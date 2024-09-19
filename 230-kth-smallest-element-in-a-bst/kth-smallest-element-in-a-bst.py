# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        temp= root
        def inorder(temp):
            if not temp:
                return 
            (inorder(temp.left))
            arr.append((temp.val))
            (inorder(temp.right))
        inorder(temp)
        return arr[k-1]



            
        