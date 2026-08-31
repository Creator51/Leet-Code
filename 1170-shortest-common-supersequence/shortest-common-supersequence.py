class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)

        dp=[[-1]*(m+1) for _ in range(n+1)]

        def lcs(i,j):

            if i==0 or j==0:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+lcs(i-1,j-1)
            else:
                dp[i][j]=max(lcs(i-1,j),lcs(i,j-1))

            return dp[i][j]
        
        #printing of LCS
        ans=[]
        print(lcs(n,m))
        i,j=n,m
        while  i>0 and j>0:

            if str1[i-1]==str2[j-1]:
                ans.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                ans.append(str1[i-1])
                i-=1
            else:
                ans.append(str2[j-1])
                j-=1

        while i > 0:
            ans.append(str1[i-1])
            i -= 1

        while j > 0:
            ans.append(str2[j-1])
            j -= 1

        return "".join(reversed(ans))

        


        