class Solution:
    # def answer(self,index,nums,dp):

    #     #This is the Dp - Meorization

    #     if index == 0:
    #         return nums[index]

    #     if index < 0:
    #         return 0

    #     if dp[index]!=-1:
    #         return dp[index]

    #     pick = nums[index] + self.answer(index-2,nums,dp)
    #     not_pick = self.answer(index-1,nums,dp)
        
    #     dp[index]=max(pick,not_pick)
    #     return dp[index]

    def rob(self, nums: List[int]) -> int:

        # Tabularization
        # dp=[-1]*(len(nums))
        # dp[0]=nums[0]

        # for i in range(1,len(nums)):

        #     pick= nums[i]
        #     if i > 1:
        #         pick+=dp[i-2]
        #     not_pick = dp[i-1]

        #     dp[i]=max(pick,not_pick)

        # return dp[len(nums)-1]

        #Space optimization

        n=len(nums)
        prev = nums[0]
        prev2 = 0

        for i in range(1,n):

            pick = nums[i] 
            if i > 1:
                pick+=prev2
            not_pick= prev

            curi = max(pick,not_pick)

            prev2=prev
            prev=curi

        return prev


        
        
        
        

