class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        check = ["999","888","777","666","555","444","333","222","111","000"]
        for i in check:
            if (i) in num:
                return (i)

        return ""
        
        