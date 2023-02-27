import unittest

from data_structures.stack.Stack import Stack


class TestStackPush(unittest.TestCase):

    def setUp(self) -> None:
        self.books = ("book_1", "book_2", "book_3")

    def test_adding_when_empty(self) -> None:
        books_stack = Stack()
        books_stack.push(self.books[0])

        self.assertEqual(books_stack._items[0], self.books[0])

    def test_adding(self) -> None:
        books_stack = Stack()

        books_stack.push(self.books[0])
        books_stack.push(self.books[1])

        self.assertEqual(books_stack._items[0], self.books[0])
        self.assertEqual(books_stack._items[1], self.books[1])

class TestStackPop(unittest.TestCase):
    def setUp(self) -> None:
        self.books = ("book_1", "book_2", "book_3")

        self.books_stack = Stack()
        self.empty_books_stack = Stack()
        for book in self.books:
            self.books_stack.push(book)

    def test_removal_empty_stack(self):
        deleted_element = self.empty_books_stack.pop()
        self.assertEqual(deleted_element, None)

    def test_removal_stack(self):
        deleted_element = self.books_stack.pop()
        self.assertEqual(deleted_element, self.books[len(self.books) - 1])
        self.assertEqual(self.books_stack._count, 2)

class TestToString(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')

        self.names_stack: Stack = Stack()
        self.names_stack_empty: Stack = Stack()
        self.names_stack_one_element: Stack = Stack()

        for name in self.names:
            self.names_stack.push(name)
        
        self.names_stack_one_element.push(self.names[0])
    
    def test_empty_stack(self) -> None:
        names_stack_empty: Stack = self.names_stack_empty        
        expected_output: str = ''
        
        self.assertEqual(names_stack_empty.to_string(), expected_output)
    
    def test_one_element_stack(self) -> None:
        names: tuple = self.names
        names_stack_one_element: Stack = self.names_stack_one_element
        expected_output: str = f'{names[0]}'

        self.assertEqual(names_stack_one_element.to_string(), expected_output)
    
    def test_multiple_elements_stack(self) -> None:
        names: tuple = self.names
        names_stack: Stack = self.names_stack
        expected_output: str = f'{names[2]}, {names[1]}, {names[0]}'
        
        self.assertEqual(names_stack.to_string(), expected_output)


