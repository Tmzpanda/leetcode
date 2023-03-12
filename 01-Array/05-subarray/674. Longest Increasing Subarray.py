# 674. Longest Increasing Subarray - 1d - greedy O(n)
def LIS(nums):
    if not nums:
        return 0
    
    longest = 1
    flag = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]: 
            flag = i
        longest = max(longest, i - flag + 1)
        
    return longest
