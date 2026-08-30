class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s

        ans=""
        l_ans=0

        for i in range(len(s)):
            l=r=i

            #for odd

            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r +=1

                
            s1=s[l+1:r]

            #for even

            l,r=i,i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1

                

            s2=s[l+1:r]
            
            #print(ans)
            #print(f"s1 is {s1} ,s2 is {s2}")
            if len(s1) > len(ans):
                ans=s1
            if len(s2)>len(ans):
                ans=s2

            #print(f"answer is {ans}")
            # if len(s1)>=len(s2) and len(s1)>=l_ans:
            #     ans+=s1
            #     l_ans=len(s)
            # else:
            #     ans+=s2
            #     l_ans=len(s)
        return ans
            

                  