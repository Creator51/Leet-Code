class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash={}
        
        for sc,tc in zip(s,t):
            if sc in hash:
                if hash[sc]!= tc:
                    return False
            elif tc in hash.values():
                return False
            
            hash[sc]=tc
        return True
        