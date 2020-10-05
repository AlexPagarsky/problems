class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        newHead, temp = ListNode(-1), head
        newHead.next = head
        nums = set(); nums.add(head.val)

        while head:
            if head.val not in nums:
                value = head.val
                nums.add(value)

                while nums.val == value:
                    temp.next = head
                    head = head.next
                temp = temp.next
            head = head.next
            
        return newHead.next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         newHead, temp = ListNode(-1), head
#         newHead.next = temp
#         nums = set()

#         while head:
#             if head.val not in nums:
#                 if temp.val != head.val:
#                     nums.add(head.val)
#                     temp.next = head
#                     temp = temp.next
#                     head = head.next
#                 else:
#                     head = head.next
#                     temp.next = head

#         return newHead.next
