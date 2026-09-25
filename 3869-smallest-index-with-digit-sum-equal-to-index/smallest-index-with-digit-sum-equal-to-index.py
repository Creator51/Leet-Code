class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        ans=-1

        def helper(n):
            ans=0
            while n:
                div=n%10
                ans+=div
                n=n//10

            return ans

        for i in range(len(nums)):

            if nums[i] >9:
                nums[i]=helper(nums[i])
            if i==nums[i]:
                ans=i
                break

        return ans


        