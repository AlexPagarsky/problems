# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        dummy = curr = ListNode(-1)

        for lst in lists:
            while lst:
                nodes.append(lst)
                lst = lst.next

        for node in sorted(nodes, key=lambda n: n.val):
            curr.next = node
            curr = curr.next

        return dummy.next

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


############################ slow one (7 actual fucking seconds)

# class Solution:

#     def mergeTwoSorted(self, lhs, rhs):
#         start = ListNode(-1)
#         end = start

#         while lhs and rhs:
#             if lhs.val < rhs.val:
#                 end.next = lhs
#                 end = end.next
#                 lhs = lhs.next
#             else:
#                 end.next = rhs
#                 end = end.next
#                 rhs = rhs.next

#         while lhs:
#             end.next = lhs
#             end = end.next
#             lhs = lhs.next

#         while rhs:
#             end.next = rhs
#             end = end.next
#             rhs = rhs.next

#         return start.next


#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0:
#             return None
#         result = lists[0]

#         for i in range(1, len(lists)):
#             result = self.mergeTwoSorted(result, lists[i])

#         return result
