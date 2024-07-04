# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        curr=head.next
        sum=0
        while curr.val!=0:
            sum+=curr.val
            curr=curr.next
        head.next.val= sum
        head.next.next= self.mergeNodes(curr)
        return head.next
            