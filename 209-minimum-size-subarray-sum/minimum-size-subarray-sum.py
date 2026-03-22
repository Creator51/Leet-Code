class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans=0
        l=0
        maxi=float('inf')

        tmp=0

        for r in range(len(nums)):


            tmp += nums[r]
            while tmp >= target:
                maxi=min(r-l+1,maxi)
                tmp-=nums[l]
                l+=1


        if maxi == float('inf'):
            return 0
        else:
            return maxi

                

            
        