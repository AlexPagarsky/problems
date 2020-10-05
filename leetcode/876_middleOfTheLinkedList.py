# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head: return None
        slow = head
        counter = 0 

        while head.next:
            if not counter % 2:
                slow = slow.next
            head = head.next
            counter += 1

        return slow