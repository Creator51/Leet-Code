class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minn = min(nums)
        maxx = max(nums)

        return k * (maxx - minn)
        