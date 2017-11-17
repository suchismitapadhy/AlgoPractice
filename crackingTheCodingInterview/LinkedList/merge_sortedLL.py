#-------------------------------------------------------------------------------
# Name:        Merge Two Sorted Lists
# Purpose:
#   Merge two sorted linked lists and return it as a new list.
#   The new list should be made by splicing together the nodes of the first
#   two lists.
#-------------------------------------------------------------------------------
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def mergeTwoLists(l1, l2):
    rst = TreeNode(0) #sentinel node
    current = rst.next
    while l1 and l2:
        if l1 < l2:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return rst.next

def print_ll(head):
    while head is not None:
        print(head.data,end=" -->")
        head = head.next
    print()


# Node Instance
newNode = Node(1)
newNode.next = Node(3)
newNode.next.next = Node(5)
p = Node(7)
newNode.next.next.next = p

newNode1 = Node(2)
newNode1.next = Node(4)
newNode1.next.next = Node(6)
q = Node(8)
newNode1.next.next.next = q

print_ll(mergeTwoLists(newNode,newNode1))

