class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                buy = prices[i]
                sell = prices[j]
                profit_new = sell - buy
                if profit_new > profit:
                    profit = profit_new

        return profit