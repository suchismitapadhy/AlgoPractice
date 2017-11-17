#-------------------------------------------------------------------------------
# Name:        Remove Duplicates from Sorted List
# Purpose:
#
#        Given a sorted linked list, delete all duplicates
#        such that each element appear only once.
#        For example,
#        Given 1->1->2, return 1->2.
#        Given 1->1->2->3->3, return 1->2->3
#-------------------------------------------------------------------------------
def deleteDuplicates(head):
    if head is None:
        return None
    current = head
    while current.next:
        post = current.next
        if current.val == post.val:
            current.next = current.next.next # Move two steps ahead
        else:
            current = post                  # Move one step
    return head
a = [1, 1, 2, 3, 3]
head = ListNode()
head.add_many(a)
b = deleteDuplicates(head)
b.show()