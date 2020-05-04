class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None  # 下一节点


class SingleLinkList(object):
    """单向链表"""
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self .__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            index = 0
            while index < pos - 1:
                index += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:
                if pre is None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            pre = cur
            cur = cur.next

    def search(self, item):
        cur = self.__head
        index = 0
        while cur is not None:
            if cur.item == item:
                return print(index)
            cur = cur.next
            index += 1
        return print(-1)
