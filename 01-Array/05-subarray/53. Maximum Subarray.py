# 53. Maximum Subarray 

# greedy O(n)
def maxSubArray(nums):
    min_sum = 0
    max_sum = -sys.maxsize
    prefix_sum = 0
    
    for num in nums:
        prefix_sum += num
        max_sum = max(prefix_sum - min_sum, max_sum)
        min_sum = min(prefix_sum, min_sum)
        
    return max_sum
