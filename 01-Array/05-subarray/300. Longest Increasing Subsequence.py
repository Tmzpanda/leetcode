# 300. Longest Increasing Subsequence - O(n^2)
# dp O(n^2)
def LIS(nums):
    if not nums:
        return 0
    
    n = len(nums)        
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)   




# binary search O(nlogn)
class Solution:
    def lengthOfLIS(self, nums):
            
        temp = [sys.maxsize] * (len(nums) + 1)
        temp[0] = -sys.maxsize
        
        longest = 0
        for num in nums:
            index = self.searchInsert(temp, num)
            temp[index] = num
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

