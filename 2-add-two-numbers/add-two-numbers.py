# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = 0
        tmp = result
        while l1 is not None or l2 is not None or curr:
            sum_node = curr
            if l1 is not None:
                sum_node += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_node += l2.val
                l2 = l2.next
            curr = sum_node // 10
            tmp.next = ListNode(sum_node % 10)
            tmp = tmp.next
        return result.next
