class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(root, value):
    if root is None:
        root = TreeNode(value)

    if root.data <= value:
        if root.right is None:
            root.right = TreeNode(value)
        else:
            insert(root.right, value)
    else:
        if root.left is None:
            root.left = TreeNode(value)
        else:
            insert(root.left, value)


b = TreeNode(20)
values = [10, 30, 2, 7, 23]
for value in values:
    insert(b, value)


