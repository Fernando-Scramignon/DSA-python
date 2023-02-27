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

        did_insertion_worked: bool = doubly_linked.insert(names[0], -2)
        self.assertFalse(did_insertion_worked)

class TestRemoveAt(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')

        self.doubly_linked: DoublyLinkedList = DoublyLinkedList()
        self.doubly_linked_one_node: DoublyLinkedList = DoublyLinkedList()
        self.doubly_linked_two_node: DoublyLinkedList = DoublyLinkedList()

        for index, name in enumerate(self.names):
            self.doubly_linked.insert(name, index)

        self.doubly_linked_one_node.insert(self.names[0], 0)

        self.doubly_linked_two_node.insert(self.names[0], 0)
        self.doubly_linked_two_node.insert(self.names[1], 1)
        
        
    
    def test_removing_index_out_of_range(self) -> None:
        doubly_linked: DoublyLinkedList = self.doubly_linked

        deleted_element: any | None = doubly_linked.remove_at(3)
        self.assertIsNone(deleted_element)

        deleted_element: any | None = doubly_linked.remove_at(-3)
        self.assertIsNone(deleted_element)

    def test_removing_first_element(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        deleted_element: any | None = doubly_linked.remove_at(0)
        self.assertEqual(deleted_element, names[0])

        new_head: DoublyNode | None = doubly_linked.get_element_at(0)
        self.assertEqual(new_head.element, names[1])
        self.assertIsNone(new_head.prev)
        self.assertEqual(doubly_linked._head, new_head)


    def test_removing_element_when_size_is_one(self) -> None:
        names: tuple = self.names
        doubly_linked_one_node: DoublyLinkedList = self.doubly_linked_one_node

        deleted_element: any | None = doubly_linked_one_node.remove_at(0)
        self.assertEqual(deleted_element, names[0])


        self.assertEqual(doubly_linked_one_node._head, None)
        self.assertEqual(doubly_linked_one_node._tail, None)

    def test_removing_first_element_when_size_is_two(self) -> None:
        names: tuple = self.names
        doubly_linked_two_node: DoublyLinkedList = self.doubly_linked_two_node

        expected_head_after_deletion: DoublyNode | None = doubly_linked_two_node.get_element_at(1)

        deleted_element: any | None = doubly_linked_two_node.remove_at(0)
        self.assertEqual(deleted_element, names[0])

        new_head: DoublyNode | None = doubly_linked_two_node.get_element_at(0)
        
        self.assertEqual(new_head, expected_head_after_deletion)
        self.assertIsNone(new_head.prev)

    def test_removing_last_element(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        doubly_last_index: int = doubly_linked.size() - 1

        while doubly_last_index > 0:
            deleted_element: any | None = doubly_linked.remove_at(doubly_last_index)
            self.assertEqual(deleted_element, names[doubly_last_index])
            
            doubly_last_index -= 1

            new_tail: DoublyNode = doubly_linked.get_element_at(doubly_last_index)
            self.assertEqual(new_tail, doubly_linked._tail)

    def test_removing_last_element_when_size_is_two(self) -> None:
        names: tuple = self.names
        doubly_linked_two_nodes: DoublyLinkedList = self.doubly_linked_two_node

        deleted_element: any = doubly_linked_two_nodes.remove_at(1)
        self.assertEqual(deleted_element, names[1])

        expected_tail: DoublyNode = doubly_linked_two_nodes.get_element_at(0)
        current_tail: DoublyNode = doubly_linked_two_nodes._tail
        self.assertEqual(expected_tail, current_tail)

    def test_removing_middle_element(self) -> None:
        names: tuple = self.names
        doubly_linked: DoublyLinkedList = self.doubly_linked

        previous_node: DoublyNode = doubly_linked.get_element_at(0)
        next_node: DoublyNode = doubly_linked.get_element_at(2)

        deleted_element: any = doubly_linked.remove_at(1)
        self.assertEqual(deleted_element, names[1])
        
        self.assertEqual(previous_node.next, next_node)
        self.assertEqual(next_node.prev, previous_node)

class TestGetElementAt(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan', 'Michael', 'Aiden', 'Robert')
        self.names_list: DoublyLinkedList = DoublyLinkedList()
        self.names_list_empty: DoublyLinkedList = DoublyLinkedList()
        self.names_list_one_element: DoublyLinkedList = DoublyLinkedList()

        for index, name in enumerate(self.names):
            self.names_list.insert(name, index)
                
        self.names_list_one_element.insert(self.names[0], 0)
    
    def test_empty_list(self) -> None:
        names_list: DoublyLinkedList = self.names_list_empty

        self.assertIsNone(names_list.get_element_at(0))
        self.assertIsNone(names_list.get_element_at(1))
        self.assertIsNone(names_list.get_element_at(-1))
        self.assertIsNone(names_list.get_element_at(-2))

    def test_one_element_list(self) -> None:
        names_list_one_element: DoublyLinkedList = self.names_list_one_element
        names: tuple = self.names
        expected_output: str = names[0]

        self.assertEqual(names_list_one_element.get_element_at(0).element, expected_output)

        self.assertIsNone(names_list_one_element.get_element_at(1))
        self.assertIsNone(names_list_one_element.get_element_at(2))
        self.assertIsNone(names_list_one_element.get_element_at(-1))
        self.assertIsNone(names_list_one_element.get_element_at(-2))
    
    def test_normal_case(self) -> None:
        names_list: DoublyLinkedList = self.names_list
        names: tuple = self.names

        for index, name in enumerate(names):
            element: str = names_list.get_element_at(index).element
            expected_output = name

            self.assertEqual(element, expected_output)

        self.assertIsNone(names_list.get_element_at(1000))
        self.assertIsNone(names_list.get_element_at(-1))

class TestPush(unittest.TestCase):
    def setUp(self) -> None:
        self.names: tuple = ('John', 'Jack', 'Ryan')
        self.names_list: DoublyLinkedList = DoublyLinkedList()
        
    def test_adding(self) -> None:
        names_list: DoublyLinkedList = self.names_list
        names: tuple = self.names

        for index, name in enumerate(names):

            added_node: DoublyNode = names_list.push(name)
            expected_element: DoublyNode = names_list.get_element_at(index)

            if index == 0:
                self.assertEqual(names_list._head == added_node)
            
            self.assertEqual(names_list._tail, added_node)

            self.assertEqual(added_node, expected_element)
            self.assertEqual(added_node.element, name)
            self.assertEqual(names_list.size(), index + 1)
