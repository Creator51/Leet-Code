class Solution:
    #Memorization
    # def helper(self,i,j,matrix,dp):

        

    #     if i==0 and j==0 :
    #         return 0 if matrix[0][0]==1 else 1

    #     if i<0 or j < 0 :
    #         return 0

    #     if dp[i][j]!=-1:
    #         return dp[i][j]

    #     if i>=0 and j>=0 and matrix[i][j]==1:
    #         return 0

    #     up=self.helper(i-1,j,matrix,dp)
    #     left=self.helper(i,j-1,matrix,dp)
    #     dp[i][j]=up+left
    #     return up+left
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid) # Rows
        n=len(obstacleGrid[0]) #Columns 
        
        dp= [[0]*n for _ in range(m)]
        # return self.helper(i-1,j-1,obstacleGrid,dp)
        #Tabulatization
        dp[0][0]= 0 if obstacleGrid[0][0]==1 else 1
        for i in range(m):
            for j in range(n):

                #obstackle
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue 

                #base
                if i==0 and j==0:
                    dp[i][j]=0 if obstacleGrid[i][j]==1 else 1
                    continue

                up,left=0,0

                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]

                dp[i][j]=up+left
        return dp[m-1][n-1]
        