class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    t = 0
    pre = None
    p = l1
    while l1 != None and l2 != None:
        t, l1.val =divmod(l1.val + l2.val + t, 10)
        pre = l1
        l1, l2 = l1.next, l2.next
    if l1 is None and l2 is None:
        if t > 0:
            end = ListNode(t)
            pre.next = end 
            end.next = None
    if l1 is None:
        l1 = l2
        pre.next = l1
    while l1 is not None:
        t, l1.val = divmod(l1.val + t, 10)
        pre = l1
        l1 = l1.next
    if t > 0:
        end = ListNode(t)
        pre.next = end 
        end.next = None
    return p