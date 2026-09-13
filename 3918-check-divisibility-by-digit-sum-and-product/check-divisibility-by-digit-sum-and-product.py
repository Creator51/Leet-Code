class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n==0:
            return False
        def help(n):
            summ=0
            prod=1
            ans=[]
            while n:
                div=n%10
                prod*=div
                ans.append(div)
                n=n//10

            summ=sum(ans)
            return summ+prod

        return True if n%help(n)==0 else False
            
        