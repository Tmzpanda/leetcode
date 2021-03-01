
1. [hashmap](https://zhuanlan.zhihu.com/p/127147909)
     - hash function: [MD5](https://en.wikipedia.org/wiki/MD5) or [SHA256](https://en.wikipedia.org/wiki/SHA-2),
     - [hash collision](https://www.jianshu.com/p/aa457757cc13): 
              - open hash：有collision就存个linked list
              - close hash：有collision就找下一个可用位置
     - [重哈希](https://www.jianshu.com/p/bdf6109ecb18)：哈希表存储的元素太多（如超过容量的十分之一），我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。 


2. [heap](https://zhuanlan.zhihu.com/p/91406647)
     - 操作：push O(logn) -> siftup, pop O(logn) -> siftdown
     - 实现：arrary


3. [Tree](https://www.zhihu.com/question/30527705)
     - rbtree: 平衡二叉搜索树，插入删除效率高，应用于TreeMap, open hash
     - AVL: 更为平衡，查询效率高
     - b树，b+树：多路平衡搜索树（大量减少重新平衡和数据迁移的次数），数据库索引（需要持久化在磁盘，同时需要大量查询和插入操作）
     - Trie: 前缀匹配

4. Queue
     - CircularArray: [代码实现](https://github.com/Tmzpanda/leetcode/blob/main/data_structure.py)
     - LinkedArrayList: append(val), appendleft(val), pop(), popleft(), get(idx), put(idx, val) -> O(1)












     

    
    



      
