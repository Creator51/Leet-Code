class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = float('-inf')
        n = len(s)
        st = 0
        end =0 
        dubli = set()

        if len(s) == 0:
            return 0

        while end < n:
            
            while s[end] in dubli:
                dubli.remove(s[st])
                st+=1

            dubli.add(s[end])
            maxi = max(maxi,end - st +1)

            end +=1

        return maxi