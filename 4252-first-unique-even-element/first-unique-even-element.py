class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        m = Counter(nums)
        for i in nums:
            if i % 2 == 0 and m[i] == 1:
                return i
        return -1