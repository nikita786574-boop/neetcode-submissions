# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        sorted_list = ListNode()
        h = sorted_list
        while list1 != None or list2 != None:
            if list1 == None:
                h.next = ListNode(list2.val)
                list2 = list2.next
                h = h.next
                continue
            if list2 == None:
                h.next = ListNode(list1.val)
                list1 = list1.next
                h = h.next
                continue
            if list1.val > list2.val:
                h.next = ListNode(list2.val)
                list2 = list2.next
                h = h.next
            else:
                h.next = ListNode(list1.val)
                list1 = list1.next
                h = h.next
        return sorted_list.next