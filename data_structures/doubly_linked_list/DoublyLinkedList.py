from data_structures.linked_list.LinkedList import Node
from data_structures.linked_list.LinkedList import LinkedList
import math
import pdb

class DoublyNode(Node):
    def __init__(self, element: any) -> None:
        super().__init__(element)
        self.prev: DoublyNode | None = None

class DoublyLinkedList(LinkedList):
    def insert(self, element: any, index: int) -> any:
        if index < 0 or index > self._count:
            return False
        
        node: DoublyNode = DoublyNode(element)

        if index == 0:
            if not self._head:
                self._head = node
                self._tail = node
                self._count += 1

                return True
            
            old_head: DoublyNode = self._head
            old_head.prev = node
            node.next = old_head            
            self._head = node

            self._count += 1
            return True
        
        if index == self._count:
            old_tail: DoublyNode = self._tail

            old_tail.next = node
            node.prev = old_tail
            self._tail = node

            self._count += 1
            return True
            
        previous: DoublyNode = self.get_element_at(index - 1)
        current: DoublyNode = previous.next

        previous.next = node
        current.prev = node
        node.prev = previous
        node.next = node

        self._count += 1
        return True
    
    def remove_at(self, index: int) -> any:
        list_last_index: int = self._count - 1

        if index < 0 or index > list_last_index:
            return None
        
        if index == 0:
            old_head: DoublyNode = self._head
            new_head: DoublyNode = old_head.next

            self._head = new_head

            if new_head:
                new_head.prev = None
            
            self._count -= 1


            if self.size() == 0:
                self._tail = None

            return old_head.element
        
        if index == list_last_index:
            old_tail: DoublyNode = self._tail
            new_tail: DoublyNode = old_tail.prev

            self._tail = new_tail
            new_tail.next = None
            self._count -= 1
            
            return old_tail.element

        deleted_node: DoublyNode = self.get_element_at(index)
        previous_node: DoublyNode = deleted_node.prev
        next_node: DoublyNode = deleted_node.next

        previous_node.next = next_node
        next_node.prev = previous_node

        self._count -= 1
        return deleted_node.element

    def get_element_at(self, index: int) -> Node:
        if index >= self._count or index < 0:
            return None
        
        current: DoublyNode
        
        middle: int =  math.floor(self.size() / 2)

        if index > middle:
            current = self._tail

            for _ in reversed(range(index, self.size() - 1)):
                current = current.prev

            return current      
        
        current = self._head
        for _ in range(index):
            current = current.next
        
        return current

    def __init__(self) -> None:
        super().__init__()
        self._tail: DoublyNode | None = None