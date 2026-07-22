class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if len(s)==0:
        #     return 0
        # s=s.split()
        # return len(s[-1])
        
        #Optimal

        if len(s)==0:
            return 0

        length=0
        i=len(s)-1

        while i>=0 and s[i]==" ":
            i-=1

        while i>=0 and s[i]!=" ":
            length+=1
            i-=1

        return length
