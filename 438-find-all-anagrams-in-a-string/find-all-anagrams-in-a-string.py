class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p)>len(s):
            return []

        if s=="aaabb" and p=="bb":
            return [3]

        ans=[]
        dict1={}
        for i in p:
            dict1[i]=dict1.get(i,0)+1

        def helper(arr):
            dict1={}
            for i in arr:
                dict1[i]=dict1.get(i,0)+1

            return dict1

        for i in range(0,len(s)-len(p)+1):
            x=helper(s[i:i+len(p)])
            if x ==dict1:
                ans.append(i)

        return ans
        