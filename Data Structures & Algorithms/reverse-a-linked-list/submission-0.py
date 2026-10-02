# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        buf = head.next
        buf1 = head
        head.next = None
        
        while buf.next != None:
            
            buffer = buf.next
            buf.next = buf1
            buf1 = buf
            buf = buffer 
            
        buf.next = buf1
        return buf