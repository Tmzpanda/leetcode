"""
duplication - sort    O(nlogn) O(1)
            - set     O(n) O(n)
            - value index mapping   O(n) O(1)

"""

# sort 
def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            return nums[i]


# set 
# deduplicate
def deduplicate(nums):
    index = 1
    traversed = set()
    for i in range(len(nums)):
        if i > 0 and nums[i] not in traversed:
            nums[index] = nums[i]
            index += 1
        traversed.add(nums[i])

    return nums[:index]


# value index mapping
"""
1 ≤ a[i] ≤ n 
0 ≤ index ≤ n - 1
<value, index> exclusive mapping makes O(n) O(1) achievable

"""

def findDuplicates(nums):
    res = []
    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            res.append(abs(nums[i]))
        nums[index] = - nums[index]
        
    return res
