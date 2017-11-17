#-------------------------------------------------------------------------------
# Name:        Add Two Numbers
# Purpose:
#   You are given two linked lists representing two non-negative numbers.
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
#-------------------------------------------------------------------------------
def addTwoNumbers(l1, l2):
    current = dummy = ListNode(0)
    carry = 0
    while l1 or l2:
        rst = carry
        if l1:
            rst += l1.val
            l1 = l1.next
        if l2:
            rst += l2.val
            l2 = l2.next
        carry = rst / 10
        rst %= 10
        current.next = ListNode(rst)
        current = current.next
    current.next = ListNode(1) if carry == 1 else None
    return dummy.next