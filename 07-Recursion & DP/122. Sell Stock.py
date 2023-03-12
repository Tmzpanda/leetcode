# 122. Sell Stock - ∞ transactions - greedy O(n) 
def maxProfit(prices):
    n = len(prices)
    profit = 0
    
    for i in range(1, n):
        if prices[i - 1] < prices[i]:
            profit += prices[i] - prices[i - 1]
            
    return profit
  