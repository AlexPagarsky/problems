# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1)

        if head is not None:
            new_head.next = head
            head = head.next
            new_head.next.next = None
        else:
            return None

        while head is not None:
            # pop node from list
            curr = head
            head = head.next
            curr.next = None

            # insert in our new list
            tmp = new_head
            while tmp.next is not None:
                print(curr.val, head.val, tmp.next.val)
                if curr.val < tmp.next.val:
                    curr.next = tmp.next
                    tmp.next = curr
                else:
                    tmp = tmp.next

        return new_head.next