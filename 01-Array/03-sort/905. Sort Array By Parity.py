# 905. Sort Array By Parity - partition O(n)
def sortArrayByParity(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        while l < r and nums[l] % 2 == 0:
            l += 1
        while l < r and nums[r] % 2 == 1:
            r -= 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    return nums