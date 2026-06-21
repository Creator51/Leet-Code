class Solution:
    # def answer(self,index):

    #     if index == 0:


    def rob(self, nums: List[int]) -> int:

        # Tabularization

        if len(nums) == 1:
            return nums[0]

        dp=[-1]*(len(nums))
        dp[0]=nums[0]

        for i in range(1,len(nums)-1):

            pick= nums[i]
            if i > 1:
                pick+=dp[i-2]
            not_pick = dp[i-1]

            dp[i]=max(pick,not_pick)
        ans1=dp[len(nums)-2]
        dp=[-1]*(len(nums))
        dp[0]=0
        dp[1]=nums[1]

        for i in range(2,len(nums)):

            pick= nums[i]
            if i > 1:
                pick+=dp[i-2]
            not_pick = dp[i-1]

            dp[i]=max(pick,not_pick)

        ans2=dp[len(nums)-1]
        return max(ans1,ans2)

        # return dp[len(nums)-1]

        

        
        