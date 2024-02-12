# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy1 = ListNode(next = head)
        dummy2 = ListNode(next = head)
        
        ans = dummy1

        while n:
            dummy2 = dummy2.next
            n -= 1
        
        while dummy2.next:
            dummy2 = dummy2.next
            dummy1 = dummy1.next
        
        temp = dummy1.next
        dummy1.next = dummy1.next.next
        temp.next = None

        return ans.next
