
class TreeNode():
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right



def LCA_BT(root,node1, node2):
    #traverse for node1
    if root is None:
        return
    if root.data == node1 or root.data==node2:
        return root
    if LCA_BT(root.left,node1, node2) and LCA_BT(root.right,node1,node2):
        return root
    if LCA_BT(root.left,node1, node2):
            return root.left
    if LCA_BT(root.right,node1,node2):
        return root.right

T = TreeNode("z", TreeNode("a",TreeNode("c"),TreeNode("d")), TreeNode("b",TreeNode("e"),TreeNode("f")))
print(LCA_BT(T, "z","d").data)

