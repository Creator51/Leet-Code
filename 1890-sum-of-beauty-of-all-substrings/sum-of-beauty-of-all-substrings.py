class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            hash={}
            for j in range(i,len(s)):
                if s[j] in hash:
                   hash[s[j]]+=1
                else:
                    hash[s[j]]=1

                maxi=max(hash.values())
                mini=min(hash.values())

                res += (maxi - mini)
        return res
                
        