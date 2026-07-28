class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix,sufix=1,1

        maxi=float('-inf')
        n=len(nums)
        for i in range(len(nums)):

            if prefix==0:
                prefix =1
            if sufix ==0:
                sufix=1

            prefix = prefix * nums[i]
            sufix = sufix * nums[n-i-1]

            maxi=max(maxi,max(prefix,sufix))

        return maxi
        