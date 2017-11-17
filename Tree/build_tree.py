from tree import TreeNode
import sys

def build_tree(preorder, inorder):
    print(preorder)
    print(inorder)
    if len(preorder)!=len(inorder):
        print("Invalid")
        sys.exit(0)
    if len(preorder)==1 and len(inorder)==1:
        return TreeNode(preorder[0])
    #preorder's 1st item is the root
    root = TreeNode(preorder[0])
    # get location of root in Inorder
    root_ix = inorder.index(root.data)
    # left of root's location is leftsubtree
    left_in = inorder[:root_ix]
    #right of root's location is right subtree
    right_in = inorder[root_ix+1:]

    left_pre = preorder[1:len(left_in)+1]
    right_pre = preorder[1+len(left_in):]

    if len(left_pre)>0:
        root.left = build_tree(left_pre, left_in)

    if len(right_pre)>0:
        root.right = build_tree(right_pre, right_in)
    return root

def main():
    preorder = ["a", "b", "d", "e", "c", "f"]
    inorder = ["d", "b", "e", "a", "f", "c"]
    build_tree(preorder, inorder)
main()

