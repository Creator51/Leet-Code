class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash={}
        hash[0]=-1
        prefix = 0
        for i,num in enumerate(nums):
            prefix += num
            rem = prefix % k 
            if rem in hash:
                if i - hash[rem] >= 2:
                    return True

            else:
                hash[rem]=i

        return False 
        