# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head

        while current is not None: 

            next_node = current.next    # saves the nodes in the list from disapearing (starts before changing any pointers)

            current.next = prev        # makes current point resverse 

            prev = current             # moves prev to a pointer that moves

            current = next_node        # moves current to contines on the list 

        return prev