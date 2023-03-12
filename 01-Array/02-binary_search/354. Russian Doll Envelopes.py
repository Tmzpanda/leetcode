# 354. Russian Doll Envelopes - binary search O(nlogn)
"""
(2, 3), (5, 3), (6, 4), (6, 7)

3, 3, 7, 4

"""
class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
            
        envelopes.sort(key=lambda x: (x[0], -x[1]))
      
        temp = [sys.maxsize] * (len(envelopes) + 1)
        temp[0] = -sys.maxsize
        
        # LIS - binary search O(nlogn)
        longest = 0
        for _, height in envelopes:
            index = self.searchInsert(temp, height)
            temp[index] = height
            longest = max(longest, index)
        
        return longest
    
    def searchInsert(self, nums, target):      
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid
        return r

# 354. Russian Doll Envelopes - dp O(n^2)
class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
            
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [x[1] for x in envelopes]
        
        return self.LIS(heights)
        
    # LIS - dp O(n^2)
    def LIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)        
        dp = [1] * len(nums)
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
