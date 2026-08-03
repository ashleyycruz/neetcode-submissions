# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Create two pointers that both start at the head
        slow = head
        fast = head

        # Continue while fast can keep moving
        while fast and fast.next:

            # Slow moves one node
            slow = slow.next

            # Fast moves two nodes
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # If fast reaches the end, there is no cycle
        return False