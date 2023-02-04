import unittest

class Node():
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList(unittest.TestCase):
    def push(self, element):
        node = Node(element)

        if not self._head:
            self._head = node
            self._count += 1
            return node

        current = self._head
        while(current.next):
            current = current.next
        
        current.next = node
        self._count += 1
        return node

    
    def insert(self, element, index):
        pass

    def get_element_at(self, index):
        if index >= self._count or index < 0:
            return None
        
        current = self._head
        for _ in range(index):
            current = current.next

        return current
        

    def remove(self, element):
        pass
    
    def index_of(self, element):
        pass

    def remove_at(self, index):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def toString(self):
        pass

    def __init__(self):
        self._head = None
        self._count = 0
        