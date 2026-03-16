class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        if len(s) == 1:
            return 1

        
        for i in range(1,len(s)):
            #odd palindorme
            low = i
            high =i
            while low >= 0 and high < len(s) and s[low]==s[high]:
                ans+=1
                low -=1
                high +=1

                if low == -1 or high == len(s):
                    break
            #even palindorme
            low = i-1
            high = i
            while low >=0 and high < len(s) and s[low]== s[high]:
                ans+=1
                low -=1
                high +=1

                if low == -1 or high == len(s):
                    break

        return ans+1
        