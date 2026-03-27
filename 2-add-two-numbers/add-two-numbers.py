class Solution:
    def addTwoNumbers(self, l1, l2):
        arr1, arr2 = [], []
        t1, t2 = l1, l2

        while t1:
            arr1.append(t1.val)
            t1 = t1.next

        while t2:
            arr2.append(t2.val)
            t2 = t2.next

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while arr1 or arr2 or carry:
            x = arr1.pop() if arr1 else 0
            y = arr2.pop() if arr2 else 0

            total = x + y + carry
            carry = total // 10

            node = ListNode(total % 10)
            curr.next = node
            curr = curr.next

        return dummy.next