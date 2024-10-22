# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sum_array = []
        def levelNum(node, lvl):
            if node is None:
                return
            if len(sum_array) == lvl:
                sum_array.append(0)
            sum_array[lvl] += node.val
            levelNum(node.left, lvl + 1)
            levelNum(node.right, lvl + 1)
        levelNum(root, 0)
        sum_array.sort()
        if len(sum_array) >= k:
            return sum_array[-k]
        return -1