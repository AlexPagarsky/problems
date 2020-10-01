# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def summ(l1, l2):
    if l1 + l2 > 10:
        carry = (l1 + l2) - 10
        val = (l1 + l2) % 10
    elif l1 + l2 == 10:
        carry = 1
        val = 0
    else:
        carry = 0
        val = l1 + l2

    return val, carry


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        out = res
        res.next = ListNode(l1.val + l2.val)
        res.next.val, carry = summ(l1.val, l2.val)

        while l1 or l2 or carry:
            res.next = ListNode(0)
            res = res.next
            if l1 and l2:
                res.val, carry = summ(l1.val, l2.val + carry)
                l1 = l1.next
                l2 = l2.next
            elif carry:
                res.val = carry
                carry = 0
            
        return out.next