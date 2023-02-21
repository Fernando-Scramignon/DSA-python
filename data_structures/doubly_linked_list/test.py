import unittest
from data_structures.doubly_linked_list.DoublyLinkedList import DoublyLinkedList, DoublyNode

class TestInsert(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')
        self.doubly_linked: DoublyLinkedList = DoublyLinkedList()

    def test_adding_first_position_when_empty(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        did_insertion_work: bool = doubly_linked.insert(names[0], 0)
        self.assertTrue(did_insertion_work)

        doubly_linked_first_node: DoublyNode = doubly_linked._head
        self.assertEqual(doubly_linked_first_node.element, names[0])
     
    def test_adding_first_position_when_not_empty(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        doubly_linked.insert(names[0], 0)

        did_insertion_work: bool = doubly_linked.insert(names[1], 0)
        self.assertTrue(did_insertion_work)

        doubly_linked_first_element: any = doubly_linked._head.element
        self.assertEqual(doubly_linked_first_element, names[1])

    def test_adding_last_position(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        for index, name in enumerate(names):
            did_insertion_work = doubly_linked.insert(name, index)
            self.assertTrue(did_insertion_work)
        
        doubly_linked_second_node: DoublyNode = doubly_linked._head.next
        doubly_linked_third_node: DoublyNode = doubly_linked_second_node.next

        self.assertEqual(doubly_linked_second_node.element, names[1])
        self.assertEqual(doubly_linked_third_node.element, names[2])
        
        

    def test_adding_middle(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        doubly_linked.insert(names[0], 0)
        doubly_linked.insert(names[2], 2)

        did_insertion_worked: bool = doubly_linked.insert(names[1], 1)
        self.assertTrue(did_insertion_worked)

        doubly_linked_middle_node: DoublyNode = doubly_linked._head.next
        self.assertEqual(doubly_linked_middle_node.element, names[1])

    def test_index_out_of_range(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        did_insertion_worked: bool = doubly_linked.insert(names[0], 1)
        self.assertFalse(did_insertion_worked)

        did_insertion_worked: bool = doubly_linked.insert(names[0] -2)
        self.assertFalse(did_insertion_worked)