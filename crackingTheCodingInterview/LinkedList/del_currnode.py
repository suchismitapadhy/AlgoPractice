class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

#Given only a pointer to a node to be deleted in a singly linked list, how do you delete it?
# Algo: Fast solution is to copy the data from the next node to the node to be deleted and delete the next node.
def del_currnode(ll,node):
    node.data = node.next.data
    node.next = node.next.next
    return ll

def delete_anynode(head, item):
    temp = head
    if temp.data == item:
        return temp.next
    while temp.next is not None and temp.next.data!= item:
        temp=temp.next
    if temp.next is None:
        print("item not found to delete")
        return -1
    temp.next = temp.next.next
    return head


def print_ll(head):
    while head is not None:
        print(head.data,end=" -->")
        head = head.next
    print()



newNode = Node(2)
newNode.next = Node(13)
newNode.next.next = Node(3)
p = Node(9)
newNode.next.next.next = p

print_ll(newNode)

#print_ll(del_currnode(newNode, newNode.next))

print_ll(delete_anynode(newNode, 13))

