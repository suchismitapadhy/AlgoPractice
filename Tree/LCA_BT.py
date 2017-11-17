from tree import TreeNode

def LCA(root, n1, n2):
    if root is None:
        return None
    if root.data==n1 or root.data==n2:
        return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)

    if left is not None and right is not None:
        return root
    if left is None and right is not None:
        return right
    if left is not None and right is None:
        return left
    if left is None and right is None:
        return None

def main():
    t = TreeNode("a")
    t.left = TreeNode("b")
    t.left.left = TreeNode("d")
    t.left.right = TreeNode("e")
    t.left.left.left = TreeNode("y")
    t.left.left.right = TreeNode("z")

    t.right = TreeNode("c")
    t.right.left = TreeNode("f")
    t.right.right = TreeNode("g")

    print(LCA(t, "d", "g").data)
main()