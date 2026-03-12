class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        if num is not "":
            a=int(num[-1])
            if a % 2 != 0:
                return num

        high=""
        for i,j in enumerate(num):
            if int(j) % 2 != 0:
                high=num[:i+1]

        return high
