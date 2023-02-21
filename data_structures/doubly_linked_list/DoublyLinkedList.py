from data_structures.linked_list.LinkedList import Node
from data_structures.linked_list.LinkedList import LinkedList

class DoublyNode(Node):
    def __init__(self, element: any) -> None:
        super().__init__(element)
        self._prev: DoublyNode | None = None

class DoublyLinkedList(LinkedList):
    # check if the index is valid, if not, return None
    def insert(self, element: any, index: int) -> any:
        pass
    
    def __init__(self) -> None:
        super().__init__()
        self._tail: DoublyNode | None = None