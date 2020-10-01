# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        dummy = res

        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next

        if l1:
            res.next = l1
        elif l2:
            res.next = l2

        return dummy.next


# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         res = ListNode(0)
#         dummy = res


#         while l1 and l2:
#             if l1.val <= l2.val:
#                 res.next = ListNode(l1.val)
#                 res = res.next
#                 l1 = l1.next
#             else:
#                 res.next = ListNode(l2.val)
#                 res = res.next
#                 l2 = l2.next

#         if l1:
#             while l1:
#                 res.next = ListNode(l1.val)
#                 res = res.next
#                 l1 = l1.next
#         elif l2:
#             while l2:
#                 res.next = ListNode(l2.val)
#                 res = res.next
#                 l2 = l2.next

#         return dummy.next
