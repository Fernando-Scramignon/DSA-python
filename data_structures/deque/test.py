import unittest

from data_structures.deque.Deque import Deque

class TestAddBack(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')
        self.names_deque: Deque = Deque()
    
    def test_add_when_empty(self) -> None:
        names_deque: Deque = self.names_deque
        names: tuple = self.names

        names_deque.add_back(names[0])

        self.assertEqual(names_deque._items[0], self.names[0])
        

    def test_add_normally(self) -> None:
        names_deque: Deque = self.names_deque
        names: tuple = self.names

        for name in names:
            names_deque.add_back(name)
        
        for index, name in enumerate(names):
            self.assertEqual(names_deque._items[index], self.names[index])

class TestAddFront(unittest.TestCase):
    def setUp(self) -> None:
        names_deque: Deque = Deque()
        names: tuple = ('John', 'Jack', 'Ryan')

    def test_add_when_empty(self):
        pass
        
    def test_add_with_many_elements(self):
        pass
