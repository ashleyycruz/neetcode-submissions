# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # node x = good --> if path from root to node 
        # contains no nodes w/ greater value than node x 
        # return the number of good nodes within the tree 
        # inculde root and nodes found (index += 1)

        # DFS 
        def dfs (node, maxVal):
            if not node:
                return 0 

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res 

        return dfs(root,root.val)    
