class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def main():
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.right = TreeNode(6)

if __name__ == "__main__":
    main()