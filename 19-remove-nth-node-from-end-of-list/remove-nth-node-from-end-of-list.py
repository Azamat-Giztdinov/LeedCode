# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = head
        x = self.getLength(head) - n
        if not x:
            return head.next
        while curr:
            if not x:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            x -= 1
        return head

    def getLength(self, head: Optional[ListNode]):
        tmp = head
        size = 0
        while tmp:
            size += 1
            tmp = tmp.next
        return size