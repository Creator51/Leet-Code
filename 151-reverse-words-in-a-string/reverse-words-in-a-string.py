class Solution:
    def reverseWords(self, s: str) -> str:

        res=s.split()
        res=res[::-1]
        ans=''
        for i in range(len(res)):
            ans+=res[i]
            if i!=len(res)-1:
                ans+=' '

        return ans 
        