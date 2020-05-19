class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    """
    cur = head 
    pre = None
    while cur:
        nextNode = cur.next
        cur.next = pre
        pre = cur
        cur = nextNode
    return pre
    """
    """递归"""
    if head is None:
        return None
    if head.next is None:
        return head
    last = reverseList(head.next)
    head.next.next = head
    head.next = None
    return last