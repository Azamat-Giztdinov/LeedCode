# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(array):
            if not array:
                return
            total_sum = 0
            for node in array:
                if not node:
                    continue
                if node.left:
                    total_sum += node.left.val
                if node.right:
                    total_sum += node.right.val

            child_array = []
            for node in array:
                cur_sum = 0
                if node.left:
                    cur_sum += node.left.val
                if node.right:
                    cur_sum +=  node.right.val

                if node.left:
                    node.left.val = total_sum - cur_sum
                    child_array.append(node.left)
                if node.right:
                    node.right.val = total_sum - cur_sum
                    child_array.append(node.right)
            bfs(child_array)
        root.val = 0
        bfs([root])
        return root
        
        
        