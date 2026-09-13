class Solution:
    def countDigits(self, num: int) -> int:
        ans=0
        digits=[]

        if num==0:
            return 0


        def get_digits(digit):
            ans=[]
            while digit:
                div = digit%10
                ans.append(div)
                digit=digit//10
            return ans

        digits=get_digits(num)

        for i in digits:
            if num%i==0:
                ans+=1

        return ans

        