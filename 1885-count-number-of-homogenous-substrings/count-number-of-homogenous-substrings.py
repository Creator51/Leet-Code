class Solution:
    def countHomogenous(self, s: str) -> int:
        ans =0
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                count =1
            ans+=count
        return (ans+1)%(pow(10,9)+7)