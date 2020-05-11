class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head: ListNode, val: int) -> ListNode:
    if head is None:
        return None
    cur = head
    pre = ListNode(None)
    while cur is not None:
        if cur == head and cur.val == val:
            head = head.next
            cur = head
            continue
        if cur.val == val:
            pre.next = cur.next
        pre = cur
        cur = cur.next
    return head
            
