class Solution:
    def helper(self,i,j,matrix,dp):

        

        if i==0 and j==0 :
            return 0 if matrix[0][0]==1 else 1

        if i<0 or j < 0 :
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]

        if i>=0 and j>=0 and matrix[i][j]==1:
            return 0

        up=self.helper(i-1,j,matrix,dp)
        left=self.helper(i,j-1,matrix,dp)
        dp[i][j]=up+left
        return up+left
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        i=len(obstacleGrid)
        j=len(obstacleGrid[0])
        
        dp= [[-1]*j for _ in range(i)]
        return self.helper(i-1,j-1,obstacleGrid,dp)
        