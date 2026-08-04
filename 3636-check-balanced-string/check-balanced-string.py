class Solution:
    def isBalanced(self, num: str) -> bool:
        e=0
        o=0

        for i in range(1,len(num),2):
            e+=int(num[i])

        for i in range(0,len(num),2):
            o+=int(num[i])

        return e==o
        