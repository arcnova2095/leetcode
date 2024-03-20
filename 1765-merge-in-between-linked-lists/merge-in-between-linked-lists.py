# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy= ListNode()
        dummy.next= list1
        start= dummy
        end= list1
        if a>b :
            return None
        
        while (a!=0):
            start= start.next
            end= end.next
            a-=1
            b-=1
        while (b!=0):
            end= end.next
            b-=1
        start.next= list2
        while start.next!=None:
            start= start.next
        start.next= end.next
        return dummy.next


        