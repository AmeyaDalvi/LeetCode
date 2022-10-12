class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        buy=0
        sell=1
        while sell<len(prices):
            if prices[sell]> prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else: 
                buy = sell
            sell+=1
        return max_profit
        
        
        
#         min_price = prices[0]
#         max_profit = 0
        
#         for i in range(1, len(prices)):
#             if min_price > prices[i]:
#                 min_price = prices[i]
#             elif prices[i] - min_price > max_profit:
#                 max_profit = prices[i] - min_price
#         return max_profit

