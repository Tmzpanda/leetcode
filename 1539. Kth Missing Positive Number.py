# 1539. Kth Missing Positive Number

# O(n)
def findKthPositive(nums: List[int], k: int) -> int:
    i, target = 0, 1
    res = []

    while i < len(nums):
        if nums[i] == target:
            i += 1
            target += 1
        elif nums[i] > target:
            k -= 1
            if k == 0:
                return target
            target += 1
        else:
            i += 1

    return nums[-1] + k
  
  
# binary search O(logn)
"""
The nice part is, the indices can be used to get the positive numbers in sorted order.
`nums[i] - (i+1)` denotes to #of missing number, i.e.
nums:            [1,3,4,6]
nums[i] - (i+1): [0,1,1,2]

binary search the largest index so that `nums[i] - (i+1) <= k`
the kth missing number is `nums[i-1] + (k - (nums[i-1] - i))` = k + i

"""

def findKthPositive(nums: List[int], k: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        missing = nums[mid] - (mid + 1)
        if missing < k:
            l = mid + 1
        else:
            r = mid - 1

    return l + k 
  
  
