class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head is None:
        return None
    p1 = head
    for _ in range(n - 1):
        if p1 is None:
            return None
        else:
            p1 = p1.next
    if p1.next == None:
        return head.next
    p2 = head
    pre = None
    while p1.next is not None:
        pre = p2
        p1 = p1.next
        p2 = p2.next
    pre.next = p2.next
    return head
    