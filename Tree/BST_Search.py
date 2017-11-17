from tree import TreeNode
def BST_Search(root, search_item):
    if root is None:
        return None
    if root.data == search_item:
        return root.data
    if root.data > search_item:
        #explore left
        root = root.left
        return BST_Search(root, search_item)
    if root.data < search_item:
        root = root.right
        return BST_Search(root, search_item)

def main():
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(2)
    t.right = TreeNode(9)
    t.right.left = TreeNode(10)
    t.right.right = TreeNode(11)

    print(BST_Search(None, 12))
if __name__ == '__main__':
    main()

# #algo : Given the root of the binary search tree and a search key to find
# if root is None -- return None
# if root is data -- return root
# else:
#     recursively search root.left if search_key is less than root or root.right if the search_key > root