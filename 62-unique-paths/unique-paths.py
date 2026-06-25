class Solution:
    #Memorization
    # def helper(self,i,j,dp):

    #     if dp[i][j]!= -1:
    #         return dp[i][j]

    #     if i==0 and j ==0 :
    #         return 1
    #     if i < 0 or j < 0:
    #         return 0

    #     up=self.helper(i-1,j,dp)
    #     left=self.helper(i,j-1,dp)

    #     dp[i][j]=up + left
    #     return up + left
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        # return self.helper(m-1,n-1,dp)

        dp[0][0]=1

        for i in range(m):
            for j in range(n):

                if i ==0 and j==0:
                    continue

                up=0
                left=0
                if i > 0:
                    up=dp[i-1][j]
                if j > 0:
                    left=dp[i][j-1]

                dp[i][j]= left + up
        return dp[m-1][n-1]
        