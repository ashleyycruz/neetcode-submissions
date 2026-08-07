# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # middle 
        slow, fast = head, head.next 

        while fast and fast.next:

            slow = slow.next # shifts by 1 
            fast = fast.next.next # shifts by 2

        second = slow.next # set for the second half
        prev = slow.next = None # set both to none 

        #resverse second half 
        while second: # while second is non Null set to prev 
            tmp = second.next
            second.next = prev 
            prev = second # second is in front but set pointer to back 
            second = tmp # put tmp after that ( which was the first value)

        #merge two halfs 
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2 

            






            

        



        
       