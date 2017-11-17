#-------------------------------------------------------------------------------
# Name:       Linked List Cycle
# Purpose:
#
#        Given a linked list, determine if it has a cycle in it.
#        Follow up:
#        Can you solve it without using extra space?
#-------------------------------------------------------------------------------
def hasCycle(head):
    fast, slow = [head]*2 # Enter runner mode with two pointers
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True
    return False

# if we have dont have a cycle fast runner will reach the end of ll before slow runner
# in case cycle is present they will meet