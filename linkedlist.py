class Linkedlist():
    # make a constructor
    def __init__(self, headNode):
        self.head = headNode

    # Add a member function to calculate length
    def get_length(self):
        count = 1
        if self.head is None:
            return 0
        temp = self.head
        while temp.next != None:
            temp = temp.next
            count += 1
        return count


class Node():
    # make a constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def partition(ll, pivot):
    temp = ll
    while temp.next != pivot:
        temp = temp.next
    pivot = temp.next
    temp.next = pivot.next
    while temp.next != None:
        temp = temp.next
    temp.next = pivot

    i = ll
    j = pivot
    flag = True
    while i != pivot:
        if i.data < pivot.data:
            if flag:
                ll = i
                flag = False
            i = i.next
        else:
            curr = i.next
            pivot.next = i
            i = curr
            j = j.next
    if flag:
        ll = pivot
    return ll


# Node Instance
newNode = Node(13)
newNode.next = Node(7)
newNode.next.next = Node(3)
p = Node(9)
newNode.next.next.next = p
# linkedlist instance
# ll = Linkedlist(newNode)

ll = partition(newNode, p)



# Tasks:
# created a structure for linkedlist
# add member fn of linkedlist to calculate length
# print elements of linkedlist
# reverse a linkedlist
# delete a node from a particular index
#

