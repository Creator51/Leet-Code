class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        def helper(n):
            ans=[1]
            for i in range(2,n+1):
                if n%i==0:
                    ans.append(i)

            return ans

        ans1=(helper(a))
        ans2=(helper(b))
        cle = set(ans1) & set(ans2)
        return len(cle)

        