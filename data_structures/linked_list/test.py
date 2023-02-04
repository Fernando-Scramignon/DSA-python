import unittest
from data_structures.linked_list.LinkedList import LinkedList

class TestGetElementAt(unittest.TestCase):
    def setUp(self) -> None:
        self.players_tuple = ("Isagi", "Bachira", "Kunigami")
        
        self.players = LinkedList()
        self.players_empty = LinkedList()

        for player in self.players_tuple:
            self.players.push(player)
    
    def test_normal_search(self):
        player_1 = self.players.get_element_at(0)
        player_2 = self.players.get_element_at(1)
        player_3 = self.players.get_element_at(2)

        self.assertEqual(player_1.element, self.players_tuple[0])
        self.assertEqual(player_2.element, self.players_tuple[1])
        self.assertEqual(player_3.element, self.players_tuple[2])

    def test_out_of_range_index(self):
        player = self.players.get_element_at(7)
        self.assertEqual(player, None)
    
    def test_empty_list(self):
        player = self.players_empty.get_element_at(0)
        self.assertEqual(player, None)
        
    


class TestPush(unittest.TestCase):
    def setUp(self) -> None:
        self.names_tuple = ("John", "Jack", "Ryan")
        self.names = LinkedList()

    def test_adding_when_empty(self):
        self.names.push(self.names_tuple[0])
        self.assertEqual(self.names.get_element_at(0).element, self.names_tuple[0])
            

    def test_adding_normaly(self):
        for name in self.names_tuple:
            self.names.push(name)
        
        for i, name in enumerate(self.names_tuple):
            self.assertEqual(self.names.get_element_at(i).element, self.names_tuple[i])

class TestIndexOf(unittest.TestCase):
    def setUp(self) -> None:
        self.players_tuple = ("Isagi", "Bachira", "Nagi")
        self.players = LinkedList()
        self.players_empty = LinkedList()

        for player in self.players_tuple:
            self.players.push(player)
    
    
    def test_search_normaly(self):
        for i, player in enumerate(self.players_tuple):
            self.assertEqual(self.players.index_of(player), i)

    def test_search_not_in_list(self):
        self.assertEqual(self.players.index_of("Barou"), None)

    def test_search_when_empty(self):
        self.assertEqual(self.players_empty.index_of("Isagi"), None)
