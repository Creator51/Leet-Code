class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans=""

        if len(word1)<len(word2):
            length = len(word1)
            rem=word2[length:] 
        else:
            length= len(word2)
            rem=word1[length:]
        

        for i in range(length):
            ans+=word1[i]
            ans+=word2[i]

        return ans+rem

        
        