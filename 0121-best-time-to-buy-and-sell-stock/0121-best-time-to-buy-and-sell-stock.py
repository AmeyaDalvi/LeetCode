class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =0
        sell = 1
        
        profit = 0
        max_profit = 0
        
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            if prices[buy]< prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit
            sell += 1
                          
            
        return max_profit
            