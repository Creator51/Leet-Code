# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Now doing it without extra Space and Reursive

        if not head or not head.next:
            return head

        #Split the list into 2 halfes Left and right

        left = head
        right = self.getmiddle(head)
        temp=right.next
        right.next=None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)

    def getmiddle(self,head):
        slow , fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self,left,right):
        dummy = ListNode(0)
        curr=dummy
        while left and right:
            if left.val < right.val:
                curr.next=left
                left=left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left :
            curr.next = left
        else:
            curr.next = right

        return dummy.next