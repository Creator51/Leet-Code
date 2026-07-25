class Solution:
    def maxProduct(self, n: int) -> int:
        ans=[]

        if len(str(n))<2:
            return n

        while n:
            temp=n%10
            ans.append(temp)
            n=n//10

        ans.sort()

        return ans[-1]*ans[-2]        
        