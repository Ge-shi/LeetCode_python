# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        st = set()
        cur = head
        pre = head
        while cur:
            if cur.val in st:
                pre.next = cur.next
                if pre:
                    cur = pre.next
                else:
                    break
            else:
                st.add(cur.val)
                pre = cur
                cur = cur.next                
        return head