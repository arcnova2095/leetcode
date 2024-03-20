"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy={}
        def dfs(node):
            if node in copy:
                return copy[node]
            temp= Node(node.val)
            copy[node]= temp
            for i in node.neighbors:
                temp.neighbors.append(dfs(i))
            return temp
        
        return dfs(node) if node else None


        