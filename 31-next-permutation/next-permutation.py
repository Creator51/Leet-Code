class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        index=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            return nums.reverse()
        
        for i in range(n-1,-1,-1):
            if nums[i] > nums[index]:
                nums[i],nums[index]=nums[index],nums[i]
                break
        start=index+1
        end=n-1
        nums[start : end + 1] = nums[start : end + 1][::-1]

       