# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next=head
        prefix=0
        p={0:dummy}
        current= head
        while current:
            prefix+= current.val
            if prefix in p:
                delete= p[prefix].next
                temp= prefix+delete.val
                while delete !=current:
                    del p[temp]
                    delete=delete.next
                    temp+=delete.val
                p[prefix].next=current.next
            else:
                p[prefix]= current
            current=current.next
        return dummy.next
