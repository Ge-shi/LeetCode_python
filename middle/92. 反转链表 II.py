class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    count = 1
    cur = head
    pre = dummy
    while count != m:
        pre = cur
        cur = cur.next
        count += 1
    # print(pre.val, cur.val, count)
    pre.next = None
    p = None 
    k = cur
    while count != n + 1:
        pN = cur.next
        cur.next = p
        p = cur 
        cur = pN
        count += 1
    # print(cur.val, pN.val)
    pre.next = p
    k.next = pN
    return dummy.next 