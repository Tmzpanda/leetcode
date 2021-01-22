"""
121. Sell Stock - Subsequence Maximum Diffs - one transaction - greedy O(n)
122.                                        - ∞ transactions - greedy O(n) 
188.                                        - at most K transactions - dp O(n*k)
309.                                        - ∞ transactions with cooldown - dp O(n)
714.                                        - ∞ transactions with transaction fee - dp O(n)

198. Rob House - Non-adjacent Elements Sum - array - dp O(n)
213.                                       - cycle - dp O(n)
337.                                       - tree - d&q O(n)

"""
# 198. House Robber - array        
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = nums[0], max(nums[0], nums[1])

        for i in range(3, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])

        return dp[n]

# 213. House Robber - cycle
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
        dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])     # nums[0: n -2]
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])     # nums[1n -1]

        for i in range(3, n):
            dp1[i] = max(nums[i - 1] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

        return max(dp1[n - 1], dp2[n - 1])

      
# 337. tree
class Solution:
    def rob(self, root):
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)
        
    def visit(self, root):
        if root is None:
            return 0, 0
        
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)
        
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob
      
      
