class Solution(object):

    def helper(self,m,n,dp):
        
        if dp[m][n]!=-1:
            return dp[m][n]
        if m==0 and n==0:
            return 1

        if m<0 or n<0:
            return 0

        up=self.helper(m-1,n,dp)
        left=self.helper(m,n-1,dp)

        dp[m][n]=up+left
        return up+left
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1]*n for _ in range(m)]
        return self.helper(m-1,n-1,dp)