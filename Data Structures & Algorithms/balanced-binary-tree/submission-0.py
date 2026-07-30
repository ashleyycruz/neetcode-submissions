# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0] # base case 

            left = dfs(root.left) # dfs for left 
            right = dfs(root.right) # dfs for right 

            balanced = (
                left[0] # left is balanced 
                and right[0] # right is balanced 
                and abs(left[1] - right[1]) <= 1 # balanced from top root 
            )

            return [balanced, 1 + max(left[1], right[1])] # boolean, height

        return dfs(root)[0]