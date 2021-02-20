kth largest
topK frequent 怎么处理dictionary 应该返回哪半部分
quickselct - quicksort 跳出条件不同
mdian of 2 sorted array - log(m+n)
recursion.py 最下面


topic - sell stock - dp state transfer
paint house
dp滚动数组


     
# Theory
1. hashmap
     - hash function: [MD5](https://en.wikipedia.org/wiki/MD5) or [SHA256](https://en.wikipedia.org/wiki/SHA-2),
     - [hash collision](https://www.jianshu.com/p/aa457757cc13): 
              - open hash：有collision就存个linked list
              - close hash：有collision就找下一个可用位置
     - [重哈希](https://www.jianshu.com/p/bdf6109ecb18)：哈希表存储的元素太多（如超过容量的十分之一），我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。 


2. [heap](https://zhuanlan.zhihu.com/p/91406647)
     - 操作：push O(logn) -> siftup, pop O(logn) -> siftdown
     - 实现：arrary


3. Tree
     - b树，b+树：多路平衡搜索树
     - rbtree: 平衡二叉搜索树，插入删除效率高，应用于TreeMap, open hash
     - AVL: 更为平衡，查询效率高
     - Trie

4. Array
     - CircularArray
     - LinkedArrayList










     

    
    



      
