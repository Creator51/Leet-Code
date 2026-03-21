class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def vovel(a):
            if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
                return True
        

        ans=0
        maxi_ans=0
        l=0
        for r in range(len(s)):
            if vovel(s[r]):
                ans+=1
            
            if r>=k :
                if vovel(s[l]):
                    ans-=1
                l+=1
            maxi_ans=max(maxi_ans,ans)


          

        return maxi_ans
            