# 448. Find All Numbers Disappeared in an Array

# O(n) space
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    nums_set = set(nums)
    res = [target for target in range(1, n + 1) if target not in nums_set]
    return res
    
    
# O(1) space
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    for num in nums:
        i = abs(num) - 1
        nums[i] = -abs(nums[i])   # mark the corresponding entries as negative
    return [i + 1 for i in range(n) if nums[i] > 0]
  


  
  # 448. Find Disappeared Numbers in an Array - O(n) O(1)
def findDisappearedNumbers(nums):
    res = []
    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = - nums[index]

    return [index + 1 for index in range(len(nums)) if nums[index] > 0]
