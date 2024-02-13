# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head

        while current:
            prev, curr_sorted = dummy, dummy.next

            while curr_sorted and curr_sorted.val < current.val:
                prev, curr_sorted = curr_sorted, curr_sorted.next
            
            temp = current.next
            current.next = curr_sorted
            prev.next = current

            current = temp

        return dummy.next
