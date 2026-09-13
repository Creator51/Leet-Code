from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=max(nums)
        y=min(nums)

        return gcd(x,y)
        