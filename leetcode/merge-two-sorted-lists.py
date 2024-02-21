# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head

        def helper(head, head1, head2):
            if not head1:
                head.next = head2
                return 
            if not head2:
                head.next = head1
                return
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
                head = head.next
            else:
                head.next = head2
                head2 = head2.next
                head = head.next

            helper(head, head1, head2)

        helper(head, list1, list2)
        
        return dummy.next