class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(l,r):

            if l>r:
                return 0

            if l==r:
                return 1

            if dp[l][r]!=-1:
                return dp[l][r]

            if s[l]==s[r]:
                dp[l][r]=2+solve(l+1,r-1)
                return dp[l][r]

            else:

                dp[l][r]=max(solve(l+1,r),solve(l,r-1))

            return dp[l][r]
        
        return solve(0,n-1)


        