class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        l3 = l1
        l3.next = mergeTwoLists(l1.next, l2)
    else:
        l3 = l2
        l3.next = mergeTwoLists(l1, l2.next)
    return l3