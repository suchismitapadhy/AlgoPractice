#Most basic question: reverse singly linked list
# Solution of iteration
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def reverse_ll(head):
    prev, current = None, head # Three pointers: previous, current and future
    while current:
        future = current.next # we would lose track so have to preserve in a dummy variable
        current.next = prev # reversing the connection
        prev = current
        current = future
    return prev

def reverse_k_elements(head,k):
    prev, current = None, head  # Two pointers: previous and current
    i=0
    while i!=k:
        future = current.next  # we would lose track so have to preserve in a dummy variable
        current.next = prev  # reversing the connection
        prev = current
        current = future
        i+=1
    head.next = current



    return prev




# # Solution of recursion
# def rvs_rcs(head):
#     if None in [head, head.next]:
#         return head
#     current = rvs_rcs(head.next)
#     head.next.next = head
#     head.next = None
#     return current


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
n6 = Node(7)
n5.next = n6

print_ll(newNode)
#print_ll(reverse_ll(newNode))
print_ll(reverse_k_elements(newNode,3))