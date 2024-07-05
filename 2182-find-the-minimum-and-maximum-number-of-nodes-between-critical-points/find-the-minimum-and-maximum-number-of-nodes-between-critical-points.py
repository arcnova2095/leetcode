# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        
        
        def critical(node, prev_val, counter):
            if not node or not node.next:
                return
            if prev_val != -1 and ((node.val < prev_val and node.val < node.next.val) or (node.val > prev_val and node.val > node.next.val)):
                arr.append(counter)
            critical(node.next, node.val, counter + 1)
        
        
        critical(head, -1, 0)
        
        if len(arr) < 2:
            return [-1, -1]
        
        min_dist = float('inf')
        for i in range(1, len(arr)):
            min_dist = min(min_dist, arr[i] - arr[i - 1])
        max_dist = arr[-1] - arr[0]
        
        return [min_dist, max_dist]