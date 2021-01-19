

# 347. Top K Frequent Elements - sort O(nlogn)
                               - heap O(nlogk)
# 215. Kth Largest Element in an Array - quick select O()





from heapq import heappush, heappop
def topk(self, nums, k):   
    if not nums:
        return

    res = []
    for num in nums:
        heappush(res, num)

        if len(res) > k:
            heappop(res)

    res.sort(reverse=True)
    return res
