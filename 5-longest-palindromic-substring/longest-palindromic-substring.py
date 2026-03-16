class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        ans= ""
        for i in range(1,len(s)):
            #odd case
            low = i
            high =i
            while low >=0 and high<len(s) and  s[low] == s[high]:
                low -=1
                high+=1

                if low == -1 or high == len(s):
                    break

            str1=s[low+1:high]

            #Even palindrome
            low = i-1
            high = i
            while low >=0 and high<len(s) and  s[low] == s[high]:
                low -= 1
                high += 1

                if low == -1 or high == len(s):
                    break
            
            str2=s[low+1:high]

            if len(str1) > len(ans):
                ans = str1
            if len(str2) > len(ans):
                ans = str2

        return ans



        
        