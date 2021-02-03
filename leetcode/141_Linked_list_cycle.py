# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        turtle, rabbit = head, head.next
        
        while rabbit:
            turtle = turtle.next
            rabbit = rabbit.next
            rabbit = rabbit.next if rabbit else None
            
            if turtle is rabbit:
                return True
        
        return False