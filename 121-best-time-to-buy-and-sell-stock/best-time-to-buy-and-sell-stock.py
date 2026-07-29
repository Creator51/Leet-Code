class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        mini=prices[0]

        maxi=0

        for i in range(len(prices)):

            if prices[i] < mini:
                mini=prices[i]

            profit=prices[i]-mini
            maxi=max(maxi,profit)

        return maxi