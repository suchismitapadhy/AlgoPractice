class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def reverse_node_pair(head):
    if head is None:
        return
    first_ptr = head
    if first_ptr.next is None:
        return head
    second_ptr = first_ptr.next
    buff = second_ptr.next
    first_ptr.next = buff
    second_ptr.next = first_ptr
    head = second_ptr
    prev = second_ptr
    first_ptr = first_ptr.next

    print(first_ptr.data)
    print(second_ptr.data)
    print(prev.data)

    while first_ptr is not None:
        if first_ptr.next is None:
            return head
        second_ptr = first_ptr.next
        buff = second_ptr.next
        first_ptr.next = buff
        second_ptr.next = first_ptr
        prev.next = second_ptr
        first_ptr = first_ptr.next
    return head







def print_ll(head):
    while head is not None:
        print(head.data,end=" -->")
        head = head.next
    print()

newNode = Node(1)
n2 = Node(4)
newNode.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(2)
n3.next = n4
n5 = Node(5)
n4.next = n5
n6 = Node(2)
n5.next = n6

print_ll(newNode)
print_ll(reverse_node_pair(newNode))
