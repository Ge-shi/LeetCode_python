class Stack(object):

    def __init__(self):
        self.__list = list()

    def isEmpty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.__list.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.__list[self.size()-1]
