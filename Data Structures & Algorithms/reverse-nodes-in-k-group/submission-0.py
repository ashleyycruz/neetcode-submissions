# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a node before head so we can reconnect the first reversed group
        dummy = ListNode(0, head)

        # This points to the node just before the group we are working on
        previous_tail = dummy

        # Keep processing groups until fewer than k nodes remain
        while True:
            # Start just before the group and look for its kth node
            kth = previous_tail

            # Move forward k times
            for i in range(k):
                
                kth = kth.next

                # If we run out of nodes, leave the remaining group unchanged
                if kth is None:
                    return dummy.next

            # Save the node immediately after this group
            next_group = kth.next

            # The group's first node will become its tail after reversal
            first = previous_tail.next

            # Start prev at the next group so the new tail connects to it
            prev = next_group

            # Start reversing from the first node of this group
            current = first

            # Stop once we have reversed all k nodes
            while current != next_group:
                # Save the next node before changing current.next
                tmp = current.next

                # Reverse this node's link.
                current.next = prev

                # Move prev and current forward for the next reversal
                prev = current
                current = tmp

            # kth was the group's last node; now it is the new first node
            previous_tail.next = kth

            # first was the group's first node; now it is the tail
            # Use it as the node before the next group.
            previous_tail = first

        