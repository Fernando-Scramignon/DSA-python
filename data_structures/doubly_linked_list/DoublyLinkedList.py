from data_structures.linked_list.LinkedList import Node
from data_structures.linked_list.LinkedList import LinkedList

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
    
    def __init__(self) -> None:
        super().__init__()
        self._tail: DoublyNode | None = None