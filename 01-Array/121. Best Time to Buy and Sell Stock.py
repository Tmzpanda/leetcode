# 121. Best Time to Buy and Sell Stock

# greedy O(n)
import sys
def maxProfit(prices):
    min_price = sys.maxsize
    max_profit = 0
    
    for price in prices:
        max_profit = max(price - min_price, max_profit)
        min_price = min(price, min_price)
            
    return max_profit
