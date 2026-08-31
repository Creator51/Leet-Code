class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp=[[-1]*len(word2) for _ in range(len(word1))]
        n,m=len(word1),len(word2)
        def lcs(i,j):

            if i <0 or j<0:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            if word1[i]==word2[j]:
                dp[i][j]=1+lcs(i-1,j-1)
                return dp[i][j]

            dp[i][j]=max(lcs(i-1,j),lcs(i,j-1))

            return dp[i][j]
        delete=n-lcs(n-1,m-1)
        insert=m-lcs(n-1,m-1)
        return delete + insert
        