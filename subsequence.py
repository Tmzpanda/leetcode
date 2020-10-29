"""
# subsequence
# sell stock - greedy O(n)
# LIS  - length - dp O(n^2)
                - binary search O(nlogn)
       - path - dp O(n^2)
# LPS O(n^2)
# LCS - dp O(n^2)




# subset
# Largest Divisible Subset - dp O(n^2)
# Russian Dolls Envelopes - dp(nlogn)

# kSum O(n^(k-1))
# combinationSum - all possible solutions - backtrack O(2^n)
                 - if possible solution exists - dp O(n*S)
                 - number of possible solutions - dp O(n*S)


                             
"""

# sell stock - greedy O(n)
import sys
def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    
    for price in prices:
        maxProfit = max(price - minPrice, maxProfit)
        minPrice = min(price, minPrice)
            
    return maxProfit




  
  
  
  






