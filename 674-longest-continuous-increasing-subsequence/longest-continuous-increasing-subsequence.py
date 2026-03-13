class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans=1
        maxx=0
        if len(nums)==1:
            return 1
        for i in range(1,(len(nums))):
            if nums[i-1] < nums[i]:
                ans+=1
            else:
                ans=1

            maxx=max(maxx,ans)  
        return maxx
        