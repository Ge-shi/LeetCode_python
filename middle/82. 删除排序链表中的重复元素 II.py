# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dt = {}
        cur = head
        while cur:
            if cur.val in dt:
                dt[cur.val] += 1
            else:
                dt[cur.val] = 1
            cur = cur.next
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if dt[cur.val] >= 2:
                pre.next = cur.next
                cur = pre.next
            elif dt[cur.val] == 1:
                pre = cur
                cur = cur.next
        return dummy.next