# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newHead, temp = ListNode(-1), head
        newHead.next = temp

        while head:
            if temp.val != head.val:
                temp.next = head
                temp = temp.next
                head = head.next
            else:
                head = head.next
                temp.next = head

        return newHead.next



# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head: return None
#         newHead, temp = ListNode(-1), head
#         newHead.next = temp

#         while head:
#             if temp.val != head.val:
#                 temp.next = head
#                 temp = temp.next
#             head = head.next

#         temp.next = head
            
#         return newHead.next



# 1 2 3 3