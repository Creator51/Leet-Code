class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount,scount={},{}

        if len(p) > len(s):
            return []

        for i in range(len(p)):
            pcount[p[i]]=pcount.get(p[i],0)+1
            scount[s[i]]=scount.get(s[i],0)+1
        res=[]
        if pcount == scount :
            res.append(0)
        
        l=0
        for r in range(len(p),len(s)):
            scount[s[r]]=scount.get(s[r],0)+1
            scount[s[l]]-=1

            if scount[s[l]] == 0:
                scount.pop(s[l])
            l+=1

            if scount == pcount:
                res.append(l)

        return res


        
            

        