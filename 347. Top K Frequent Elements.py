# 347. Top K Frequent Elements   
# sort O(nlogn)
def topKFrequent(nums, k):
  
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: -x[1])
    # most_freq_element = max(freq_dict.keys(), key=lambda x: freq_dict[x])
    
    res = []
    for i in range(k):
        res.append(freq_dict_sorted[i][0])
        
    return res
  
  
# heap O(nlogk)
from heapq import heappush, heappop
def topKFrequent(nums, k):
        
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    heap = []
    for item in freq_dict.items():
        heappush(heap, (item[1], item[0]))
        if len(heap) > k:
            heappop(heap)
            
    res = []
    while len(heap) > 0:
        freq, num = heappop(heap)
        res.append(num)
        
    res.reverse()
    return res
