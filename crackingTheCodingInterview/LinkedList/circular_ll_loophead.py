#-------------------------------------------------------------------------------
# Name:       Linked List Cycle II
# Purpose:
#
#        Given a linked list, return the node where the cycle begins.
#        If there is no cycle, return null.

# #-------------------------------------------------------------------------------

# Algorithm
# -------------
# maintain a slow pointer and a fast pointer
# If both meet indicates there is a cycle
# Now start the slowptr from the head. keep fastptr where it is and start moving both by 1.
# Where they meet is the start of the cycle.
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def find_start(ll):
    slow_ptr = ll
    fast_ptr = ll

    while fast_ptr is not None and slow_ptr is not None:
        slow_ptr = slow_ptr.next
        # we dont want to access None.next
        if fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
        else:
            fast_ptr = None
        if fast_ptr == slow_ptr:
            slow_ptr = ll
            break

    if fast_ptr is None:
        print("No cycle")
        return None

    #move both pointers by 1
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr




newNode = Node(1)
n2 = Node(2)
newNode.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n4.next = n2


if find_start(newNode) is not None:
    print(find_start(newNode).data)

