class Queue:

    def size(self):
        return self._count - self._lowest_index
    
    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        return self._items[self._lowest_index]

    def enqueue(self, element):
        self._items[self._count] = element
        self._count += 1

    def dequeue(self):
        if self._lowest_index == self._count:
            return None
        
        deleted_element = self._items.pop(self._lowest_index)
        self._lowest_index += 1

        return deleted_element
    
    def to_string(self) -> str:
        if self.is_empty():
            return ''
    
        output: list = []
        
        for index in range(self.size()):
            output.append(self._items[index])
        
        output_str: str = ', '.join(output)
        return output_str

    def __init__(self):
        self._items = {}
        self._count = 0
        self._lowest_index = 0