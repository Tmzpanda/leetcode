"""


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right



def sampleBinaryTree() -> TreeNode:
    """
             1
           /   \
          2     3
         / \   /
        4   5 6
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)

    root = node_1
    node_1.left, node_1.right = node_2, node_3
    node_2.left, node_2.right = node_4, node_5
    node_3.left = node_6
    
    return root


def sampleBinarySearchTree() -> TreeNode:
    """
             8
           /   \
          3    10  
         / \   / \
        1   6 9   14
    """

    node_8 = TreeNode(8)
    node_3 = TreeNode(3)
    node_10 = TreeNode(10)
    node_1 = TreeNode(1)
    node_6 = TreeNode(6)
    node_9 = TreeNode(9)
    node_14 = TreeNode(14)

    root = node_8
    node_8.left, node_8.right = node_3, node_10
    node_3.left, node_3.right = node_1, node_6
    node_10.left, node_10.right = node_9, node_14

    return root



def sampleNarySearchTree() -> TreeNode:
    """
                1
           /  /   \  \ 
          2  3     4  5
         /| \
        6 7 8
    """

    return


def inorder_traverse(root):

    def rec(node):
        if node is None:
            return

        rec(node.left)
        res.append(node.val)
        rec(node.right)

        # return

    res = []    # closure
    rec(root)
    return res


