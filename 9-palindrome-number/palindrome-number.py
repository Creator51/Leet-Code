class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False

        def rev(n):
            rev=0
            while n:
                div=n%10
                rev =rev *10 + div
                n=n//10

            return rev

        return x==rev(x)

        