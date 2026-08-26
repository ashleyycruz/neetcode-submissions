# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # base case 
        if root is None:
            return 0 

        '''
        use DFS to find the depth of the left side
        once a node hits node
        recursion comes back upward
        '''
        left_side = self.maxDepth(root.left)

        '''
        use DFS to find the depth of the right side
        once a node hits node
        recursion comes back upward
        '''
        right_side = self.maxDepth(root.right)

        # choose the deeper side ( chooses the bigger side )
        depth = max(left_side, right_side) + 1 
        
        # return depth value 
        return depth

