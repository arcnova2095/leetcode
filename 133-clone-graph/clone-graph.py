"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy={}
        def dfs(node):
            if node in copy:
                return copy[node]
            temp= Node(node.val)
            copy[node]= temp
            for n in node.neighbors:
                temp.neighbors.append(dfs(n))
            return temp
        
        return dfs(node) if node else None
            




        