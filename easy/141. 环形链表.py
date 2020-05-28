# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        while head:
            if head.val == 'bjfuvth':
                return True
            else:
                head.val = 'bjfuvth'
            head = head.next
        return False
        """
        """
        mp = set()
        while head:
            if head in mp:
                return True
            else:
                mp.add(head)
            head = head.next
        return False
        """
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or slow is None:
                return False
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
        return True