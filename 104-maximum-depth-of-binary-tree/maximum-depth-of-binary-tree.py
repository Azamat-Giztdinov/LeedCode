# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        layer_nodes = [root]
        lvl = 0
        while layer_nodes:
            next_layer_nodes = []
            for node in layer_nodes:
                if node.left:
                    next_layer_nodes.append(node.left)
                if node.right:
                    next_layer_nodes.append(node.right)
            lvl += 1
            layer_nodes = next_layer_nodes
        return lvl
                
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))