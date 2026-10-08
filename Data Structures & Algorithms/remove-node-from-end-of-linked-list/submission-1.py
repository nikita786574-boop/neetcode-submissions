# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        buffer = head
        if buffer is None:
            return buffer
        if buffer.next is None:
            return None
        cnt = 0
        while buffer.next is not None:
            buffer = buffer.next
            cnt += 1
        index = 0
        buf = head
        back = head
        while index != cnt + 1 - n:
            back = buf
            buf = buf.next
            index += 1
        if index ==0 :
            return head.next
        buffer = buf.next
        back.next = buffer
        return head


    
        
        