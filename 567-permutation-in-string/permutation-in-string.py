class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1=len(s1)
        s1 = "".join(sorted(s1))
        if len1 > len(s2):
            return False

        def sort(a):
            a="".join(sorted(a))
            return a

        for i in range(len(s2) - len1 +1):
            if sort(s2[i:i+len1]) == s1:
                return True

        return False

        