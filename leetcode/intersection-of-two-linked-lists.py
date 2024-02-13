# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        partA = headA
        partB = headB
        list1_len = 0
        list2_len = 0

        while headA:
            list1_len += 1
            headA = headA.next
        while headB:
            list2_len += 1
            headB = headB.next
        
        if list1_len > list2_len:
            while list1_len > list2_len:
                partA = partA.next
                list1_len -= 1
        
        if list1_len < list2_len:
            while list1_len < list2_len:
                partB = partB.next
                list2_len -= 1

        while partA and partB:
            if partA == partB:
                return partA
            partA = partA.next
            partB = partB.next

        return None