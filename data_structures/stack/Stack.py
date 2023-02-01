class Stack:
    def push(self, element: any) -> None:
        self._items[self._count] = element
        self._count += 1
    
    def pop(self) -> any:
        deleted_element = self._items.pop(self._count - 1, None)

        if deleted_element:
            self._count -= 1

        return deleted_element
    
    def size(self) -> int:
        return self._count
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def peek(self) -> any:
        return self._items[self.size() - 1]
    
    def clear(self) -> None:
        self._items = {}
        self._count = 0

    def __init__(self) -> None:
        self._items = {}
        self._count = 0

if __name__ == "__main__":
    stack = Stack()
