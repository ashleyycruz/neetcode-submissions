# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        store = 0

        def dfs(root):
            if root is None:
                return 0

            nonlocal store

            # find height of left side
            left = dfs(root.left)

            # find height of right side
            right = dfs(root.right)

            # check whether left + right
            # creates a new largest diameter
            store = max (store, left + right)

            # return the HEIGHT of this subtree
            # so the parent can use it
            return max(left, right) + 1 

        dfs(root)
        return store 
      