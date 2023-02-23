# 1539. Kth Missing Positive Number
class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        
        target = 1
        res = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                i += 1
                target += 1
            elif nums[i] > target:
                res.append(target)
                target += 1
            else:
                i += 1

        if len(res) >= k: 
            return res[k - 1]

        else:
            return nums[-1] + k - len(res)

        
