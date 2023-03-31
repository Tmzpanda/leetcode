# 416. Partition Equal Subset Sum - if possible 
# O(n*S)
def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    possible_sums = set([0])
    for num in nums:
        for s in list(possible_sums):
            possible_sums.add(s + num)
    
    return target_sum in possible_sums
    

# dp O(n*S)
def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]     # dp[i][s] represents whether it's possible to obtain a sum of s using the first i numbers in nums
    for i in range(len(nums) + 1):
        dp[i][0] = True
        
    for i in range(1, n + 1):
        for s in range(target_sum + 1):
            if nums[i-1] <= s:
                dp[i][s] = dp[i-1][s-nums[i -1]] or dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s]

    return dp[n][target_sum]

    
# dp O(n*S), O(S)
def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)     # dp[s] represents whether it's possible to obtain a sum of s using the numbers in nums
    dp[0] = True
    
    for num in nums:
        for s in range(target_sum, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target_sum]

