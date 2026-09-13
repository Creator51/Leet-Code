class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        

        def split(num):
            ans=[]
            while num:
                div=num%10
                ans.append(div)
                num=num//10

            return ans

        while num>9:
            
            num=sum(split(num))

        return num


        