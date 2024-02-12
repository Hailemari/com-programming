# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left_head = ListNode()
        less_dummy = left_head
        right_head = ListNode()
        right_dummy = right_head

        while head:
            if head.val < x:
                left_head.next = head
                left_head = left_head.next
            else:
                right_head.next = head
                right_head = right_head.next
            head = head.next

        right_head.next = None
        left_head.next = right_dummy.next
        

        return less_dummy.next