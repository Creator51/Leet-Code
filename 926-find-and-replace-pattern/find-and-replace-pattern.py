class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def check(s, t):
            map_s = {}
            map_t = {}

            for a, b in zip(s, t):

                if a not in map_s:
                    map_s[a] = b

                if b not in map_t:
                    map_t[b] = a

                if map_s[a] != b or map_t[b] != a:
                    return False

            return True

        result = []
        for w in words:
            if check(w, pattern):
                result.append(w)

        return result