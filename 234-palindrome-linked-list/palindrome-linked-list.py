# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow= head,head
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
        curr= head
        prev= None
        while curr and curr!=slow:
            temp= curr.next
            curr.next= prev
            prev= curr
            curr= temp
        if fast:
            slow= slow.next
        curr= prev
        while curr and slow:
            if (curr.val!= slow.val):
                return False
            curr= curr.next
            slow= slow.next
        return True

                