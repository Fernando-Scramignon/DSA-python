import unittest
from data_structures.queue.Queue import Queue

class TestEnqueue(unittest.TestCase):
    def setUp(self) -> None:
        self.names = ("John", "Jack", "Ryan")

    def test_adding_when_empty(self):
        name_queue = Queue()
        name_queue.enqueue(self.names[0])

        self.assertEqual(name_queue._items[0], self.names[0]) 

    def test_adding(self):
        name_queue = Queue()

        for name in self.names:
            name_queue.enqueue(name)
        
        for index, name in enumerate(self.names):
            self.assertEqual(name_queue._items[index], name)

class TestDequeue(unittest.TestCase):
    def setUp(self) -> None:
        self.names = ("John", "Jack", "Ryan")
        self.names_2  = ("Billy", "Kyle", "Jerry")

        self.names_queue = Queue()
        for name in self.names:
            self.names_queue.enqueue(name)
        
        self.names_queue_one_person = Queue()
        self.names_queue_one_person.enqueue(self.names[0])

        self.names_queue_empty = Queue()
    
    def test_removing(self):
        deleted_element = self.names_queue.dequeue()
        self.assertEqual(deleted_element, self.names[0])

        deleted_element = self.names_queue.dequeue()
        self.assertEqual(deleted_element, self.names[1])
        
        self.assertEqual(self.names_queue.size(), 1)
        self.assertEqual(self.names_queue._items[self.names_queue._lowest_index], "Ryan")

    def test_removing_when_only_one_left(self):
        deleted_element = self.names_queue_one_person.dequeue()
        self.assertEqual(deleted_element, self.names[0])

        self.assertEqual(self.names_queue_one_person.size(), 0)
    
    def test_removing_while_empty(self):
        deleted_element = self.names_queue_empty.dequeue()
        self.assertEqual(deleted_element, None)
    
    def test_removing_adding_removing_again(self):

        for _ in self.names:
            self.names_queue.dequeue()
        
        for name in self.names_2:
            self.names_queue.enqueue(name)
        
        for index, name in enumerate(self.names_2):
            self.assertEqual(self.names_queue._items[index + 3], name)

class TestToString(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')
        self.names_queue: Queue = Queue()
        self.names_queue_empty: Queue = Queue()
        self.names_queue_one_element: Queue = Queue()

        for name in self.names:
            self.names_queue.enqueue(name)
        
        self.names_queue_one_element.enqueue(self.names[0])
    
    def test_empty_queue(self) -> None:
        names_queue_empty: Queue = self.names_queue_empty
        expected_output: str = ''

        self.assertEqual(names_queue_empty.to_string(), expected_output)
    
    def test_one_element_queue(self) -> None:
        names: tuple = self.names
        names_queue_one_element: Queue = self.names_queue_one_element
        expected_output = f'{names[0]}'

        self.assertEqual(names_queue_one_element.to_string(), expected_output)
    
    def test_normal_case(self) -> None:
        names: tuple = self.names
        names_queue = self.names_queue
        expected_output = f'{names[0]}, {names[1]}, {names[2]}'

        self.assertEqual(names_queue.to_string(), expected_output)
      