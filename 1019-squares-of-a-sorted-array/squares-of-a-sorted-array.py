class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_new=[]
        for i in nums:
            nums_new.append(i*i)

        nums_new.sort()
        
        return nums_new

        