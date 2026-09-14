class Solution:
    def firstUniqChar(self, s: str) -> int:
        ind=-1

        dictt={}

        for i in range(len(s)):
            dictt[s[i]]=dictt.get(s[i],0)+1
        unq=False
        for i in dictt.keys():
            if dictt[i]==1:
                unq=i
                break

        if unq:
            for i in range(len(s)):
                if s[i]==unq:
                    ind=i
                    break
        
        return ind
        