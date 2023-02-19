import unittest

class Node():
    def __init__(self, element: any) -> None:
        self.element: any = element
        self.next: Node | None = None

class LinkedList(unittest.TestCase):
    def push(self, element: any) -> Node:
        node: Node = Node(element)

        if not self._head:
            self._head = node
            self._count += 1
            return node

        current: Node = self._head
        while(current.next):
            current = current.next
        
        current.next = node
        self._count += 1
        return node

    def insert(self, element: any, index: int) -> bool:
        if index < 0 or index > self.size():
            return False
        
        new_node: Node = Node(element)

        if index == 0:
            if self.size() > 0:
                old_head: Node = self._head

                self._head = new_node
                self._head.next = old_head
                
                self._count += 1
                return True

            self._count += 1
            self._head = new_node
            return True
        
        previous_node: Node = self.get_element_at(index - 1)
        next_node: Node = previous_node.next

        previous_node.next = new_node
        new_node.next = next_node

        self._count += 1
        return True

    def get_element_at(self, index: int) -> Node:
        if index >= self._count or index < 0:
            return None
        
        current: Node = self._head
        for _ in range(index):
            current = current.next

        return current
        

    def remove(self, element: any) -> any:
        index: int = self.index_of(element)
        return self.remove_at(index)
    
    def index_of(self, element: any) -> int:
        current: Node = self._head
        c: int = 0
        while(current):
            if current.element == element:
                return c

            current = current.next
            c += 1
            
        return -1

    def remove_at(self, index: int) -> any:
        if index < 0 or index >= self._count:
            return None
        
        if self.is_empty():
            return None

        if index == 0:
            current_node: Node = self._head
            self._head = current_node.next

            self._count -= 1
            return current_node.element
        
        previous_node: Node = self.get_element_at(index - 1)
        current_node: Node = previous_node.next

        previous_node.next = current_node.next

        self._count -= 1
        return current_node.element


    def is_empty(self) -> bool:
        return self._count == 0

    def size(self) -> int:
        return self._count

    def to_string(self):
        pass

    def __init__(self):
        self._head: Node | Node = None
        self._count: int = 0
        