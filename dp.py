"""
# Fibonacci O(n)

# optimization - opt(i) = max(A, B), where A = v(i) + opt(prev(i)), B = opt(i - 1)
# rob  O(n)
# rob - houses are arranged in a circle  O(n)
# knapsack  O(n*S)
# combinationSum - if possible solution exists  O(n*S)
# combinationSum - number of possible solutions O(n*S)
  
# Longest Increasing Subsequence  O(n^2)

"""

#********************************* Fibonacci **********************************************
# Fibonacci
def fib(n):   
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
    


#********************************* combinatorial optimization **********************************************
# rob
def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    n = len(nums)
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = nums[0], max(nums[0], nums[1])
    
    for i in range(3, n + 1):
        dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
    
    return dp[n]
    
    
# rob - houses are arranged in a circle
def rob2(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    n = len(nums)
    dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
    dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])     # nums[0: n -1]
    dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])     # nums[1: n]

    for i in range(3, n):
        dp1[i] = max(nums[i - 1] + dp1[i - 2], dp1[i - 1])
        dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

    return max(dp1[n - 1], dp2[n - 1])
    
    
# knapsack  O(n*S)
def knapSack(wt, val, W): 
    n = len(wt)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                dp[i][w] = 0
                
            elif wt[i-1] <= w: 
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], 
                               dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 
  
    return dp[n][W] 


# combinationSum - if possible solution exists  O(n*S)
def combinationSum(arr, S):
    n = len(arr)
    dp = [[False for _ in range(S + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for s in range(S + 1):
            if s == 0:
                dp[i][s] = True
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i -1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
   
    return dp[n][S]


# combinationSum - number of possible solutions O(n*S)
def combinationSum(arr, S):
    n = len(arr)
    dp = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for s in range(S + 1):
            if s == 0:
                dp[i][s] = 1
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i -1]] + dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][S]



#********************************* Longest Increasing Subsequence ****************************************
# Longest Increasing Subsequence  O(n^2)
def LIS(nums):
    if not nums:
        return 0
    
    n = len(nums)        
    dp = [1] * len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                dp[j] = max(dp[j], dp[i] + 1)
                
    return max(dp)









    










