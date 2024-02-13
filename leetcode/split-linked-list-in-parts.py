# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Determine the size of each part and additional nodes
        part_size = length // k
        additional_nodes = length % k

        # Step 3: Traverse the linked list to split it into k parts
        current = head
        parts = []
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < additional_nodes else 0)

            # Move to the end of the current part
            for _ in range(part_length - 1):
                if current:
                    current = current.next

            # Set the next node as None to separate the current part
            if current:
                next_node = current.next
                current.next = None
                current = next_node

            # Add the current part to the list of parts
            parts.append(part_head)

        # Step 4: Return the array of parts
        return parts