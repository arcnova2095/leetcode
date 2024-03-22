# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        curr= head
        while curr!=None:
            arr.append(curr.val)
            curr= curr.next
        i=0
        j= len(arr)-1
        while (i<j and arr[i]==arr[j]):
            i+=1
            j-=1
        if i>=j:
            return True
        else:
            return False
                