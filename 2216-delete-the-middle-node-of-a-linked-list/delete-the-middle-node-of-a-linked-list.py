# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is  None:
            return None
        first=head
        second=head
        while first is not None and first.next is not None:
            first=first.next.next
            track=second
            second=second.next

        track.next=second.next
        return head
            
