class Solution:
    def mirrorDistance(self, n: int) -> int:
        if n == 0 :
            return 0

        def rev(n):
            
            rev=0 
            while n != 0 :
                temp = n%10
                rev = rev * 10 + temp
                n=n//10
            return rev
        
        return abs(n-rev(n))