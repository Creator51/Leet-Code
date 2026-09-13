class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_div=[]
        div=[]
        for i in range(1,n+1):

            if i%m==0:
                div.append(i)
            else:
                not_div.append(i)
        print(not_div)
        return sum(not_div)-sum(div)

        