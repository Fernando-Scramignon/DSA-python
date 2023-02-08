import unittest
import pdb

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
        index = self.index_of(element)
        return self.remove_at(index)
    
    def index_of(self, element):
        current = self._head
        c = 0
        while(current):
            if current.element == element:
                return c

            current = current.next
            c += 1
            
        return -1

    def remove_at(self, index):
        if index < 0 or index >= self._count:
            return None
        
        if self.is_empty():
            return None

        if index == 0:
            current_node = self._head
            self._head = current_node.next

            self._count -= 1
            return current_node.element
        
        previous_node = self.get_element_at(index - 1)
        current_node = previous_node.next

        previous_node.next = current_node.next

        self._count -= 1
        return current_node.element



    def is_empty(self):
        return self._count == 0

    def size(self):
        return self._count

    def toString(self):
        pass

    def __init__(self):
        self._head = None
        self._count = 0
        