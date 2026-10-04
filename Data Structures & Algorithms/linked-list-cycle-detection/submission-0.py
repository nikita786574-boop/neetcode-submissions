# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        flag = False
        if not head:
            return False
        while head.next != None:
            if getattr(head, 'flag', 0) != 0:
                flag = True
                break
            head.flag = 1
            head = head.next
        return flag