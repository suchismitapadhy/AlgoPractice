from tree import TreeNode

# DFS binary tree traversal --> preorder, inorder, postorder

def preorder(root):
    if root is None:
        return
    print(root.data, end=",")
    if root.left is not None:
        preorder(root.left)
    if root.right is not None:
        preorder(root.right)

def inorder(root):
    if root is None:
        return

    if root.left is not None:
        preorder(root.left)
    print(root.data, end=",")
    if root.right is not None:
        preorder(root.right)

def postorder(root):
    pass

def levelorder(root):
    levelq = []
    traversed_list = []
    levelq.insert(0, [root, 0])
    while len(levelq) > 0:
        curr = levelq.pop()
        curr_node = curr[0]
        level = curr[1]
        traversed_list.append([curr_node.data, level])
        if curr_node.left is not None:
            levelq.insert(0, [curr_node.left, level+1])
        if curr_node.right is not None:
            levelq.insert(0, [curr_node.right, level+1])
    return level, traversed_list

def find_leaves(root):
    levelq = []
    traversed_dict = {}
    levelq.insert(0, [root, 0])
    while len(levelq) > 0:
        curr = levelq.pop()
        curr_node = curr[0]
        level = curr[1]

        traversed_dict[level]=traversed_dict.get(level,[])+[curr_node.data]
        if curr_node.left is not None:
            levelq.insert(0, [curr_node.left, level+1])
        if curr_node.right is not None:
            levelq.insert(0, [curr_node.right, level+1])
    return traversed_dict[level]


def boundary(root):
    # return one edge
    left_edge = []
    curr = root
    while curr is not None:
        left_edge.append(curr.data)
        curr = curr.left
    leaf = find_leaves(root)
    curr = root
    right_edge = []
    while curr is not None:
        right_edge.append(curr.data)
        curr = curr.right

    return left_edge+leaf[1:-1]+right_edge[::-1]



def main():
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.left.left = TreeNode(6)
    t.left.right = TreeNode(8)
    t.right = TreeNode(9)
    t.right.left = TreeNode(11)
    t.right.right = TreeNode(3)

    level , traversed_list = (levelorder(t))
    print(traversed_list)

    # for i in range(1, len(traversed_list)):
    #     if traversed_list[i][1] == level:
    #         print(traversed_list[i][0])
    print(find_leaves(t))
    print(boundary(t))

    preorder(t)
    print()
    inorder(t)



if __name__ == "__main__":
    main()