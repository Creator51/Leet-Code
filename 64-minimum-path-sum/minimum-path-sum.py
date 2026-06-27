class Solution:
    # def helper(self,i,j,grid,dp):

    #     if dp[i][j]!=-1:
    #         return dp[i][j]

    #     if i==0 and j==0 :
    #         return grid[i][j]

    #     if i<0 or j<0 :
    #         return float('inf')

    #     up = grid[i][j] + self.helper(i-1,j,grid,dp)
    #     left = grid[i][j] + self.helper(i,j-1,grid,dp)

    #     dp[i][j]= min(up,left)
    #     return min(up,left)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        dp = [[-1] * n for _ in range(m)]
        # return self.helper(i-1,j-1,grid,dp)
        #Tabulation 
        dp[0][0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0 :
                    dp[i][j]= grid[i][j]
                    continue

                up = float('inf')
                left = float('inf')              

                if i>0:
                    up = grid[i][j] + dp[i-1][j]
                if j>0:
                    left = grid[i][j] + dp[i][j-1]

                dp[i][j]=min(up,left)

        return dp[m-1][n-1]

        