import unittest

from data_structures.deque.Deque import Deque
import pdb


class TestAddBack(unittest.TestCase):
    def setUp(self) -> None:
        self.names = ['John', 'Jack', 'Ryan']
        self.names_deque = Deque()
    
    def test_add_when_empty(self):
        names_deque = self.names_deque
        names = self.names

        names_deque.add_back(names[0])

        self.assertEqual(names_deque._items[0], self.names[0])
        

    def test_add_normally(self):
        names_deque = self.names_deque
        names = self.names

        for name in names:
            names_deque.add_back(name)
        
        for index, name in enumerate(names):
            self.assertEqual(names_deque._items[index], self.names[index])

        
        
