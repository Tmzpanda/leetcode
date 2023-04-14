# 209. Minimum Size Subarray Sum
def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    window_sum = 0
    shortest = sys.maxsize

    start = 0
    for i in range(n):
        window_sum += nums[i]
        while window_sum >= target:
            shortest = min(shortest, i - start + 1)
            window_sum -= nums[start]
            start += 1

    return shortest if shortest != sys.maxsize else 0
