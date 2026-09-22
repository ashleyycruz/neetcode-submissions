# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case 
        if not lists or len(lists) == 0: 
            return None 

        while len(lists) > 1: 
            mergedLists = []

            for i in range (0, len(lists), 2):
                L1 = lists[i]
                L2 = lists[i + 1] if (i+1) < len(lists) else None 
                mergedLists.append(self.mergeList(L1, L2))
            lists = mergedLists
        return lists[0]      

    def mergeList(self, L1, L2):

        #dummy nodes to prevent from empty list 
        dummy = ListNode()
        tail = dummy # setting to start 

        # check vals of two list 
        while L1 and L2: 
        
            if L1.val < L2.val: # if L1 is less than L2
                tail.next = L1 # set tail to L1
                L1 = L1.next # update list one pointer 
            else: # L2 is less than L1
                tail.next = L2 
                L2 = L2.next # update list two pointer 

            tail = tail.next # update tail

        if L1: # if not null & more number remaining 
            tail.next = L1 # return the rest of L2

        elif L2: # if not null & more number remaining
            tail.next = L2 # return the rest of L1

        return dummy.next
        # grab the bigger value and put into list

    


        





        