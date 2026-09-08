class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt=0

        for i in range(len(s)):
            left=right=i

            while left>=0 and right<len(s)  and s[left]==s[right]:
                left-=1
                right+=1
                cnt+=1

            left,right=i,i+1

            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                cnt+=1

        return cnt


        