# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        size = 0

        current = head
        while current:
            size += 1
            current = current.next
        
        decimal = 0
        size -= 1
        while head:
            decimal += (2 ** size)*head.val
            size -= 1
            head = head.next

        return decimal