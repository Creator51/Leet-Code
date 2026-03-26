# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None

        if head.next is None:
            return None

        while fast and fast.next:
            
            fast=fast.next.next
            track = slow
            slow= slow.next

        track.next = slow.next

        return head


        