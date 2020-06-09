from functools import lru_cache
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        def merge(l1: ListNode, l2:ListNode) -> ListNode:
            dummy = ListNode(-1)
            p = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            p.next = l1 if l2 == None else l2
            return dummy.next
        """暴力
        ans = None
        for i in lists:
            ans = merge(ans, i)
        return ans
        """
        n = len(lists)
        m = n // 2
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        else:
            return merge(self.mergeKLists(lists[::m]), self.mergeKLists(lists[m::]))