class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans1=""
        n=len(s)
        ans2=""
        ans=""
        for i in range(n):

            left,right=i,i

            while left>=0 and right < n and s[left]==s[right]:
                
                left-=1
                right +=1
            ans1=s[left+1:right]
            left,right=i,i+1
            while left>=0 and right < n and s[left]==s[right]:
                
                left-=1
                right+=1
            ans2=s[left+1:right]
        
            if len(ans1) > len(ans):
                ans=ans1
            if len(ans2)>len(ans):
                ans=ans2

        return ans


        