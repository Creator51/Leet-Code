class Solution:
    def minInsertions(self, s: str) -> int:
        
        n=len(s)
        dp=[[-1]*n for _ in range(n)]

        def lognest_palindromic_sub(i,j):

            if i>j:
                return 0

            if i==j:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]

            if s[i]==s[j]:
                dp[i][j]=2+lognest_palindromic_sub(i+1,j-1)

                return dp[i][j]

            else:
                dp[i][j]=max(lognest_palindromic_sub(i+1,j),lognest_palindromic_sub(i,j-1))

            return dp[i][j]

        return n-lognest_palindromic_sub(0,n-1)

        