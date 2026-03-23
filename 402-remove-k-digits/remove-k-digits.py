class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]

        for c in num:

            while k > 0 and stack and stack[-1] > c:
                k-=1
                stack.pop()

            stack.append(c)

        # what if all the number occurs in increasing order?
        # fix here
        if k > 0:
            stack = stack[:-k]
        res = "".join(stack)

        #return 0 if the stack is Non Empty or else return 0
        res = res.lstrip('0')
        return res if res else "0"

        
        