class Sort(object):

    def __init__(self, item):
        self.item = item

    def bubble_sort(self, alist):
        """冒泡排序"""
        length = len(alist)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]

    def insert_sort(self, alist):
        """插入排序"""
        length = len(alist)
        for i in range(1, length):
            while i-1 >= 0 and alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1

    def choose_sort(self, alist):
        """选择排序"""
        length = len(alist)
        for i in range(length):
            index = i
            for j in range(i+1, length):
                if alist[j] < alist[index]:
                    index = j
            alist[i], alist[index] = alist[index], alist[i]

    def quick_sort(self, alist, begin, end):
        if end <= begin:
            return
        temp = alist[begin]
        left = begin
        right = end
        while right > left:
            while right > left and alist[right] >= temp:
                right -= 1
            while right > left and alist[left] <= temp:
                left += 1
            alist[left], alist[right] = alist[right], alist[left]
        alist[begin] = alist[left]
        alist[left] = temp
        self.quick_sort(alist, begin, left - 1)
        self.quick_sort(alist, left + 1, end)
