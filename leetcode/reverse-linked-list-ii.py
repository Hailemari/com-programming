# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        initial_head = head
        dummy = ListNode(next = head)
        new_right = right - left
        prev_node = ListNode(next = head)
        while left - 1:
            prev_node = prev_node.next
            head = head.next
            left -= 1
        
        right_node = head
        while new_right:
            right_node = right_node.next
            new_right -= 1

        right_half_head = right_node.next # 5
        right_node.next = None # 4

        
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        
        prev_node.next = right_node
        head.next = right_half_head
        
        if head == initial_head:
            return prev_node.next
        return dummy.next

        