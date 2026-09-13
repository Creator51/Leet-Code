from math import gcd
class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        g=gcd(a,b)
        ans=0

        for i in range(1,g+1):
            if g%i==0:
                ans+=1
        return ans
        