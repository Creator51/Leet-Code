class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(s,t):
            hash={}
            for i,j in zip(s,t):
                if i in hash:
                    if hash[i]!=j:
                        return False
                elif j in hash.values():
                    return False
                hash[i]=j
            return True

        result=[]
        for i in words:
            if check(i,pattern):
                result.append(i)
        return result
        