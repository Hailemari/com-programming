# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        tail = head
        prev = ListNode(next = head)

        while tail.next:
            tail = tail.next
            prev = prev.next

        prev.next = None
        tail.next = prev

        self.reverseList(head)

        return tail
        