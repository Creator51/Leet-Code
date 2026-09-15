class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1={}


        for i in magazine:
            dict1[i]=dict1.get(i,0)+1

        for i in ransomNote:

            if i in dict1:
                dict1[i]-=1
                if dict1[i]==0:
                    del dict1[i]
            else:
                return False

        return True
        