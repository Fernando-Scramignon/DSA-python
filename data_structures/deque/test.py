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
        self.names_deque: Deque = Deque()
        self.names: tuple = ('John', 'Jack', 'Ryan')

    def test_add_when_empty(self) -> None:
        names_deque: Deque = self.names_deque
        names: tuple = self.names

        names_deque.add_front(names[0])
        self.assertEqual(names_deque._items[0], names[0])
        
    def test_add_with_many_elements(self):
        names_deque: Deque = self.names_deque
        names: tuple = self.names

        for name in names:
            names_deque.add_front(name)
        
        
        for index in reversed(range(names_deque._count - 1)):
            self.assertEqual(names_deque._items[index], name)

class TestRemoveBack(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')

        self.deque: Deque = Deque()
        self.empty_deque: Deque = Deque()

        for name in self.names:
            self.deque.add_back(name)            
    
    def test_remove_back(self):
        deque: Deque = self.deque
        names: tuple = self.names

        for index in reversed(range(3)):
            deleted_element: str = deque.remove_back()
            self.assertEqual(deleted_element, names[index])
        
        self.assertTrue(deque.is_empty())

    def test_remove_when_empty(self):
        empty_deque: Deque = self.deque
        deleted_element: any | None = empty_deque.remove_back()

        self.assertIsNone(deleted_element)