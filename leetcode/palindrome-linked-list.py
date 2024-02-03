# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Helper function to reverse a linked list
        def reverse_linked_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half_reversed = reverse_linked_list(slow)
        
        # Compare the first half with the reversed second half
        while second_half_reversed:
            if head.val != second_half_reversed.val:
                return False
            head = head.next
            second_half_reversed = second_half_reversed.next
        
        return True
