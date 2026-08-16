class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while buy < sell and sell < len(prices):
            profit_new = prices[sell] - prices[buy]
            print(profit_new, prices[sell], prices[buy])
            if profit_new < 0:
                buy = sell
                sell = buy + 1
            else:
                sell += 1
            profit = max(profit_new, profit)

        return profit
            