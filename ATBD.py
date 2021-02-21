kth largest
topK frequent 怎么处理dictionary 应该返回哪半部分
quickselct - quicksort 跳出条件不同
mdian of 2 sorted array - log(m+n)
recursion.py 最下面


topic - sell stock - dp state transfer
paint house
dp滚动数组



击鼓传花 具体方案backtrack -> 树上backtrack（两个dfs）
		方案个数dp (代码)
	
	
stack单调栈


hashmap value排序
    

# ********************************************* return **********************************************************    
# recursion top-down with return
def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        return partition(nums, start, r, k)
    if k >= l:
        return partition(nums, l, end, k)
        
    return nums[k]


# recursion top-down
def kthSmallest(nums, k):
    partition(nums, 0, len(nums - 1), k - 1)

    return nums[k - 1]


def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        partition(nums, start, r, k)
    if k >= l:
        partition(nums, l, end, k)

