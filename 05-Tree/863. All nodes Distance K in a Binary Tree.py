# 863. All nodes Distance K in a Binary Tree - bfs O(n)
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        nodeToParent = {}
        self.findParent(root, None, nodeToParent)
        
        queue = deque([target])
        seen = {target}
        level = 0
        while queue:
            if level == K:
                return [node.val for node in queue]
           
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for nextNode in (node.left, node.right, nodeToParent[node]): 
                    if nextNode and nextNode not in seen:
                        seen.add(nextNode)
                        queue.append(nextNode)    
                        
        return []
        
    def findParent(self, root, parent, nodeToParent):       # traverse
        node = root
        if node:
            nodeToParent[node] = parent
            self.findParent(node.left, node, nodeToParent)
            self.findParent(node.right, node, nodeToParent)