# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        if head == None or head.next == None:
            print("no cycle")
            return None
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                print("no cycle")
                return None
            slow = slow.next            
            fast = fast.next.next
        node = slow
        count = 1
        while node.next != slow:
            node = node.next 
            count += 1
        # print(count)
        p1 = p2 = head
        while count:
            p1 = p1.next
            count -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        """
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
            node = node.next
        return None