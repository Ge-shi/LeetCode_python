class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head: ListNode) -> bool:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)
    n = len(res)
    m = 0
    while m < n and res[m] == res[n]:
        n -= 1
        m += 1
    return m >= n
    