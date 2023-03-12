

# 297. Serialize and Deserialize Binary Tree - bfs
#                                            - dfs
class Codec:
    def serialize(self, root):
        if root is None:
            return ""

        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        while bfs_order[-1] == '#':
            bfs_order.pop()

        return "[%s]" % ','.join(bfs_order)  # "[8,3,10,1,6,#,14,#,#,4,7,13]"


    def deserialize(self, data):

        if data == "[]":
            return None

        vals = data[1:-1].split(',')  # ['8', '3', '10', '1', '6', '#', '14', '#', '#', '4', '7', '13']
        root = TreeNode(int(vals[0]))
        queue = [root]
        index = 0
        is_left_child = True

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if is_left_child:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not is_left_child:
                index += 1

            is_left_child = not is_left_child

        return root
    
   
# dfs
class Codec:

    def serialize(self, root):   
        def dfs(root):
            if not root:
                res.append("#")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper(queue):
            if queue[0] == "#":
                queue.popleft()
                return
            root = TreeNode(queue.popleft())
            l = helper(queue)
            r = helper(queue)
            root.left = l
            root.right = r
            return root
        
        tree = data.split(",")
        queue = collections.deque(tree)
        return helper(queue)
    
