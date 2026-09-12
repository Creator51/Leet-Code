class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(' ')
        ans=[]
        for i in s:
            if i=='':
                continue
            
            ans.append(i)

        return len(ans[-1])
        


        