# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head 

        while fast and fast.next: #fast is stated 
            slow = slow.next # slow is stated
            fast = fast.next.next # fast goes two ahead 

            if slow == fast: # if slow meets fast
                return True  # there is loop because they meet

        return False  # if it doesn't reach no loop  
        