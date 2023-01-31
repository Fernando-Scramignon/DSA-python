class Stack:
    def push(self, element: any) -> None:
        self._items[self._count] = element
        self._count += 1
    
    def pop(self) -> any:
        deleted_element = self._items.pop(self._count - 1, None)

        if deleted_element:
            self._count -= 1

        return deleted_element
    
    def size(self):
        return self._count
    
    def isEmpty(self):
        return self.size() == 0
        
    def __init__(self):
        self._items = {}
        self._count = 0

if __name__ == "__main__":
    stack = Stack()
