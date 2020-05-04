class Queue(object):

    def __init__(self):
        self.__list = list()

    def isempty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        if self.isempty():
            return None
        return self.__list.pop
