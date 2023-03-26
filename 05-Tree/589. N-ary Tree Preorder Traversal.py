# 589. N-ary Tree Preorder Traversal

def preorder(self, root: Optional[TreeNode]) -> List[int]:
    def dfs(root):
        if node is None:
            return
        res.append(node.val)
        for node in node.children:
            dfs(node)

    res = []
    dfs(root)
    return res
  
  
