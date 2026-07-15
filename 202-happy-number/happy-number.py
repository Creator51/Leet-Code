class Solution:
    def helper(self,n):
        ans=0
        while n:
            temp=n%10
            temp=temp**2
            ans+=temp
            n=n//10

        return ans



    def isHappy(self, n: int) -> bool:
        visited=set()
        while n not in visited:
            visited.add(n)
            n=self.helper(n)
            if n==1:
                return True

        return False

        