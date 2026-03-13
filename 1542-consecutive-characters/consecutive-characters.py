class Solution:
    def maxPower(self, s: str) -> int:
        max = 0
        tmp=0
        for i in range(1,len(s)):
            
            if s[i]==s[i-1]:
                tmp+=1
            else:
                tmp=0
            if tmp>max:
                max=tmp
        return max+1
