class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        minimum = prices[0]
        maxi=0
        for i in range(1,len(prices)):

            if prices[i] < minimum:
                minimum=prices[i]

            profit = prices[i] - minimum
            maxi=max(profit,maxi)

        return maxi

        