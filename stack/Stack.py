class Stack:
    def push(self, element: any) -> None:
        self._items[self._count] = element
        self._count += 1
    
    def pop(self) -> any:
        pass


    def __init__(self):
        self._items = {}
        self._count = 0

if __name__ == "__main__":
    stack = Stack()
