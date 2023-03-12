
# 1438. Longest Subarray With Absolute Diff at most K - sliding window O(n)
from collections import deque
import sys 

class Solution:
    def longestSubarray(self, nums, limit):
        maxq, minq = deque(), deque()
        start = 0
        longest = -sys.maxsize 

        for end in range(len(nums)):
          
            while maxq and nums[end] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[end])

            while minq and nums[end] < minq[-1]:
                minq.pop()
            minq.append(nums[end])

            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[start]:
                    maxq.popleft()
                if minq[0] == nums[start]:
                    minq.popleft()
                start += 1

            longest = max(longest, end - start + 1)

        return longest