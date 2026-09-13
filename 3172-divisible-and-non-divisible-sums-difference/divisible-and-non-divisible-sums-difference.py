class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_div=0
        div=0
        for i in range(1,n+1):

            if i%m==0:
                div+=i
            else:
                not_div+=i
        
        return (not_div)-(div)

        