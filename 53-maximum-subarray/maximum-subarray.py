class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        ans=0
        for i in nums:
            ans+=i
            if ans > maxi:
                maxi=ans
            if ans<0:
                ans=0
            
        return maxi
                
        