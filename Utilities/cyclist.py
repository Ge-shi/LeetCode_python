class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class cycSingleLinklist(object):

    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head is None

    def length(self):
        if self.isEmpty():
            return 0
        cur = self.__head
        cnt = 1
        while cur != self.__head:
            cnt += 1
            cur = cur.next
        return cnt

    def travel(self):
        if self.isEmpty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def add(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        if pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            index = 0
            while index < pos - 1:
                cur = cur.next
                index += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.isEmpty():
            return
        cur = self.__head
        pre = None
        if cur.item == item:
            while cur.next != self.__head:
                pre = cur
                cur = cur.next
            if pre is None:
                self.__head = None
            else:
                cur.next = self.__head.next
                self.__head = self.__head.next
        else:
            while cur.next != self.__head:
                pre = cur
                cur = cur.next
                if cur.item == item:
                    pre.next = cur.next
                    return
            if cur.item == item:
                pre.next = self.__head

    def search(self, item):
        if self.isEmpty():
            return False
        cur = self.__head
        while cur.next != self:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False
