class Deque:
    def add_front(self, element: any) -> any:
        
        if self.is_empty():
            return self.add_back(element)
        
        if self._lowest_index == 0:

            # from the end of the deque, shift each element to the right
            for index in reversed(range(self._count - 1)):
                self._items[index + 1] = self._items[index]
            
            self._items[self._lowest_index] = element
            return element
        
        self._items[self._lowest_index - 1] = element
        self._lowest_index -= 1
        return element
        
    def add_back(self, element: any) -> any:
        self._items[self._count] = element
        self._count += 1
        return element

    def remove_front(self):
        pass
    
    def remove_back(self) -> any:
        if self.is_empty():
            return None
        
        last_index: int = self._count - 1
        deleted_element: any = self._items.pop(last_index, None)

        self._count -= 1
        return deleted_element


    def peek_front(self) -> any:
        return self._items[self._lowest_index]

    def peek_back(self) -> any:
        return self._items[self._count - 1]

    def size(self) -> int:
        return self._count - self._lowest_index

    def is_empty(self) -> bool:
        return self._count == self._lowest_index


    def to_string(self) -> str:
        if self.is_empty():
            return ''
        
        # Using a list and joining afterwards reduce the time complexity
        output: list = []

        for index in range(self._count):
            output.append(self._items[index])
        
        str_output: str = ", ".join(output)

        return str_output

    def __init__(self) -> None:
        self._count: int = 0
        self._lowest_index: int = 0
        self._items: dict = {}
