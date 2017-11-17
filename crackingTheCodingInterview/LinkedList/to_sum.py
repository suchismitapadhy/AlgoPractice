class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def to_sum(l1,l2):
    sent = Node(0)
    current = sent
    overflow = 0

    while l1 or l2:
        total = overflow
        if l1:
            total += l1.data
            l1 = l1.next
        if l2:
            total+= l2.data
            l2 = l2.next

        if total > 9:
            overflow = 1
            current.next = Node(total - 10)
        else:
            current.next = Node(total)
        current = current.next

    if overflow!=0:
        current.next = Node(overflow)

    return sent.next

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

print_ll(to_sum(newNode,newNode1))
