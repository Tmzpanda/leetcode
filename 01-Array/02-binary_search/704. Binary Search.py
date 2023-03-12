# binary search
# https://www.programiz.com/dsa/binary-search
# iteration
def binary_search(nums, target) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# binary search recursion
def binary_search(nums, target) -> int:

    def rec(nums, l, r, target):
        if r >= l:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return rec(nums, target, mid + 1, r)
            else:
                return rec(nums, target, l, mid - 1)

        else:
            return -1

    return rec(nums, 0, len(nums)-1, target)



def binary_search_leftmost(nums: list, tartget: int) -> int:
    return 0


def binary_search_righttmost(nums: list, tartget: int) -> int:
    return 0



# 704. Binary Search
# Target
def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:     # based on nums[mid]?target
            return mid
        if nums[mid] < target:
            l = mid
        else:
            r = mid

    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1