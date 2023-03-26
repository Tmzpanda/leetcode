# 590. N-ary Tree Postorder Traversal

def postorder(root) -> List[int]:
    def dfs(node):
        if node is None:
            return
        for child in node.children:
            dfs(child)
        res.append(node.val)


    res = []
    dfs(root)
    return res
