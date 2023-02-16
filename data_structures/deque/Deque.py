class Deque:
    def add_front(self, element):
        pass
    
    def add_back(self, element):
        self._items[self._count] = element
        self._count += 1
        return element

    def remove_front(self):
        pass

    def remove_back(self):
        pass

    def peek_front(self):
        return self._items[self._lowest_index]

    def peek_back(self):
        return self._items[self._count - 1]

    def size(self):
        return self._count - self._lowest_index

    def is_empty(self):
        return self._count == self._lowest_index

    def to_string(self):
        pass

    def __init__(self):
        self._count = 0
        self._lowest_index = 0
        self._items = {}
