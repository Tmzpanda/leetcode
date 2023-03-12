# 560. Subarray with Sum Equals - K - hashmap O(n)
def subarraySum(nums, k):
    
    n = len(nums)
    psum = 0
    psum_freq_dict = defaultdict(int)
    psum_freq_dict[0] = 1
    res = 0
    
    for i in range(n): 
        psum += nums[i]
        if psum - k in psum_freq_dict:
            res += psum_freq_dict[psum - k]
            
        psum_freq_dict[psum] += 1
     
    return res