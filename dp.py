"""
O(n)
# 198. Rob House - maximum profit = dp O(n)
# 91. Decode Ways - number of solutions - dp O(n)
# 309. Sell Stocck - max profit - ∞ transactions with cooldown - dp O(n)
# 276. Paint Fence - number of solutions - dp O(n)

O(n*k)
# 256. Paint House - minimum cost - dp O(n*k)

O(n^2) 
# 139. Word Break - if possible - dp O(n^2)
                  - number of solutions - dp O(n^2)
# 300. Longest Increasing Subsequence - O(n^2)
# 354. Russian Doll Envelopes - maximum number - dp O(n^2)
                                               - binary search O(nlogn)
# 368. Largest Divisible Subset - one possible solution - dp O(n^2)
# 132. Palindrome Partitioning - minimum cut - dp O(n^2)

O(k*n) 
# 188. Sell Stock - maximum profit - at most K transactions - dp O(k*n) 
# 999. Pass the Flower - number of paths - dp O(k*n) 
                       - all possible paths - backtrack O(2^m)
                       
O(k * n^2)  
# 410. Split Array Largest Sum - dp O(k * n^2)        

                                            
O(n*S)
# knapsack
# 416. Partition Equal Subset Sum - if possible - dp O(n*S)
# 518. Coin Change - number of solutions - dp O(n*S)
# 494. Assign symbols to Target Sum - number of solutions - dp O(n*S)
                     
O(S*n) 
# 377. Combination Sum - number of solutions - different sequences are counted as different combinations - dp O(S*n)
# 322. Coin Change - fewest coins - dp O(S*n)

O(m*n)
# 688. Knight Probability in Chessboard - dp O(K*n^2)
# 221. Maximal Square - dp O(n^2) 
# 62. Unique Paths - number of solutions - dp O(m*n)
# 1143. Longest Common Subsequence - dp O(n^2)  
# 583. Delete Distance - dp(m*n)
# 516. Longest Palindromic Subsequence - dp O(n^2)
# 44. Wildcard Matching - if match - dp O(m*n)

                
space optimization:
dp[i][j] only depends on previous row, so we can optimize the space by using 2 rows instead of the matrix

      w
      0 1 2 3 4 5 6 7
 wt 0 0 0 0 0 0 0 0 0
    1 0
    3 0
    4 0   #         #
    5 0             x =  max(dp[i-1][w-wt[i-1]] + val[i-1], dp[i-1][w]), when wt[i-1] <= w
 
"""

