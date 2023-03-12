                          
# 437. Binary Tree Subpath Sum - number of solutions - psum
# bottom-up
class Solution:
    def pathSum(self, root, target):
        self.count = 0      
        self.dfs(root, 0, {0: 1}, target)
        
        return self.count

    def dfs(self, root, psum, psum_to_freq, target):
        if not root:
            return 
        
        psum += root.val
        if psum - target in psum_to_freq:
            self.count += psum_to_freq[psum - target]
    
        psum_to_freq[psum] = psum_to_freq.get(psum, 0) + 1
        self.dfs(root.left, psum, psum_to_freq, target)
        self.dfs(root.right, psum, psum_to_freq, target)
        psum_to_freq[psum] -= 1 


# top-down
class Solution(object):
    def pathSum(self, root, target):
        psum_to_freq = {0:1}
        return self.dfs(root, 0, target, psum_to_freq)

    def dfs(self, root, psum, target, psum_to_freq):
        if not root:
            return 0

        res = 0
        psum += root.val
        if psum - target in psum_to_freq:
            res += psum_to_freq[psum - target]
        
        psum_to_freq[psum] = psum_to_freq.get(psum, 0) + 1
        res += self.dfs(root.left, psum, target, psum_to_freq)
        res += self.dfs(root.right, psum, target, psum_to_freq)
        psum_to_freq[psum] -= 1

        return res