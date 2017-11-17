
class TreeNode():
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right

def LCA_BST(root,node1,node2):
    if root is None:
        return None
    if root.data == node1 or root.data==node2:
        return root
    if root.data>node1 and root.data>node2:
        return LCA_BST(root.left, node1,node2)

    if root.data<node1 and root.data<node2:
        return LCA_BST(root.right, node1, node2)

    if (root.data<node1 and root.data>node2) or (root.data<node2 and root.data>node1):
        return root



T = TreeNode(5, TreeNode(3,TreeNode(2),TreeNode(1)), TreeNode(7,TreeNode(6),TreeNode(8)))
print(LCA_BST(T, 6,8).data)
