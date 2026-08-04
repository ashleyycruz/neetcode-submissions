# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # check if both zero 
        if not p and not q:
            return True

        # check one if zero else return false 
        if not p or not q: 
            return False

        # check if value is the same 
        if p.val != q.val:
            return False 

        # check left and right childern and return result 

        return(self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))



        