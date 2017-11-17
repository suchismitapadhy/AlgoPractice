class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def kthTolast(ll,k):
    ptr1 = ll
    ptr2 = ll
    i = 0
    while i!=k:
        ptr2=ptr2.next
        i+=1
    while ptr2 is not None:
        ptr1=ptr1.next
        ptr2=ptr2.next
    return ptr1.data


def print_ll(head):
    while head is not None:
        print(head.data)
        head = head.next



newNode = Node(2)
newNode.next = Node(13)
newNode.next.next = Node(3)
p = Node(9)
newNode.next.next.next = p

print(kthTolast(newNode,3))