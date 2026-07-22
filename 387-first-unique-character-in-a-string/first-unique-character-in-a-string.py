from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict={}

        for i in s:
            dict[i]=dict.get(i,0)+1

        for i,ch in enumerate(s):
            if dict[ch]==1:
                return i

        return -1

        