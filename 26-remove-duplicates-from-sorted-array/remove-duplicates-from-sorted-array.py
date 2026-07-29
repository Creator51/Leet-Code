class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        write=0

        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                write+=1

                nums[write]=nums[i]

        return write+1
        