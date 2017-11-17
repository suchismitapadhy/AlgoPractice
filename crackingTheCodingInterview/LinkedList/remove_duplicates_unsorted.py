class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def remove_duplicates(ll):
    if ll is None:
        return None
    itemset = set()
    itemset.add(ll.data)
    temp = ll.next
    prev = ll
    while temp is not None:
        if temp.data not in itemset:
            itemset.add(temp.data)
        else:
            prev.next = temp.next
        temp = temp.next
        prev = prev.next
    return ll

def print_ll(head):
    while head is not None:
        print(head.data)
        head = head.next



newNode = Node(13)
newNode.next = Node(13)
newNode.next.next = Node(3)
p = Node(9)
newNode.next.next.next = p

print_ll(remove_duplicates(newNode))