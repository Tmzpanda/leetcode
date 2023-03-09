
# Iterator
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        res = node

        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left

        return res
