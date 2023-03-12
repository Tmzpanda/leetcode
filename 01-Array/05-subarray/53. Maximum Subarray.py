# 53. Maximum Subarray - greedy O(n)
def maxSubArray(nums):
    min_sum, max_sum = 0, -sys.maxsize
    prefix_sum = 0
    
    for num in nums:
        prefix_sum += num
        max_sum = max(max_sum, prefix_sum - min_sum)
        min_sum = min(min_sum, prefix_sum)
        
    return max_sum