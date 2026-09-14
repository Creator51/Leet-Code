class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        
        def rev(arr):
            rev=[]

            for i in arr:
                temp=list(i)
                temp.reverse()
                rev.append("".join(temp))

            return " ".join(rev)

        return rev(s)



        