#-------------------------------------------------------------------------------
# Name:        Partition List
# Purpose:
#
#        Given a linked list and a value x, partition it such that all
#        nodes less than x come before nodes greater than or equal to x.
#        You should preserve the original relative order of the nodes
#        in each of the two partitions.
#        For example,
#        Given 1->4->3->2->5->2 and x = 3,
#        return 2 -->2 -->1 -->3 -->4 -->5.
#-------------------------------------------------------------------------------
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def partition(ll, x):
    temp = ll
    prev = None
    while temp != x and temp is not None:
        prev = temp
        temp=temp.next

    if temp is None:
        print("x is not valid")
        return None
    # remove the pivit element
    prev.next = temp.next
    new_ll = temp
    new_ll.next = None

    #start again
    ptr = ll
    end = new_ll
    while ptr is not None:
        if ptr.data < x.data:
            # insert in the beginning of new_ll
            buff = ptr.next
            ptr.next = new_ll
            new_ll = ptr
            ptr = buff
        elif ptr.data == x.data:
            # insert right after pivot
            buff = ptr.next
            ptr.next = x.next
            x.next = ptr
            ptr = buff

        else:
            # insert at the end of new_ll
            buff = ptr.next
            end.next = ptr
            end = end.next
            end.next = None
            ptr = buff
    return new_ll

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
print_ll(partition(newNode, n3))


