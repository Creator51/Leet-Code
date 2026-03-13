class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        hash={}
        if len(pattern) != len(s):
            return False
        for sc,tc in zip(pattern,s):
            if sc in hash:
                if hash[sc]!=tc:
                    return False
            elif tc in hash.values():
                return False

            hash[sc]=tc
        return True

        