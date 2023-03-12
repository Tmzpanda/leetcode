# 368. Largest Divisible Subset - one possible solution - dp O(n^2)
def largestDivisibleSubset(nums):
    if not nums:
        return []
    
    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] % nums[i] == 0:
                if dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    prev[j] = i
      
    path = []
    longest = max(dp)
    index = dp.index(longest)

    while index != -1:
        path.append(nums[index])
        index = prev[index]
        
    return path[::-1]
    