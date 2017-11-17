import sys
def apply_operator(A, B, op):
    if op == "+":
        return A + B
    if op == "-":
        return A - B
    if op == "*":
        return A * B
    if op == "/":
        return A / B


def evaluate_expression_tree(root):
    if root is None:
        return
    operator = ["+", "-", "*", "/"]
    if root.left is None and root.right is None:  # we can say the current node is child/leaf(no left; no right)
        return root.data
    if root.data in operator:
        return apply_operator(evaluate_expression_tree(root.left),
                              evaluate_expression_tree(root.right), root.data)
    else:
        print("Invalid expression tree")
        sys.exit(0)


class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


T = TreeNode("+", TreeNode(3))
T.right = TreeNode("*", TreeNode("+", TreeNode(5), TreeNode(9)), TreeNode(2))
print(evaluate_expression_tree(T))