class Solution:
    def helper(self,i,j,grid,dp):

        if dp[i][j]!=-1:
            return dp[i][j]
            
        if i==0 and j==0 :
            return grid[i][j]

        if i<0 or j<0 :
            return float('inf')

        up = grid[i][j] + self.helper(i-1,j,grid,dp)
        left = grid[i][j] + self.helper(i,j-1,grid,dp)

        dp[i][j]= min(up,left)
        return min(up,left)
    def minPathSum(self, grid: List[List[int]]) -> int:
        i=len(grid)
        j=len(grid[0])

        dp = [[-1] * j for _ in range(i)]
        return self.helper(i-1,j-1,grid,dp)
        