#-------------------------------------------------------------------------------
# Name:        Sort List
# Purpose:
#   Sort a linked list in O(n log n) time using constant space complexity.
#-------------------------------------------------------------------------------
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        arr = self.ll_to_lst(head)
        head = ListNode(arr[0])
        current = head
        for x in arr[1:]:
            current.next = ListNode(x)
            current = current.next
        return head

    def ll_to_lst(self, head):
        rst = []
        while head:
            rst.append(head.val)
            head = head.next
        return sorted(rst)