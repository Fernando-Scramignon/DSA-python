import unittest
from data_structures.linked_list.LinkedList import LinkedList

class TestGetElementAt(unittest.TestCase):
    def setUp(self) -> None:
        self.players_tuple: tuple = ('Isagi', 'Bachira', 'Kunigami')
        
        self.players: LinkedList = LinkedList()
        self.players_empty: LinkedList = LinkedList()

        for player in self.players_tuple:
            self.players.push(player)
    
    def test_normal_search(self) -> None:
        player_1: str | None = self.players.get_element_at(0)
        player_2: str | None = self.players.get_element_at(1)
        player_3: str | None = self.players.get_element_at(2)

        self.assertEqual(player_1.element, self.players_tuple[0])
        self.assertEqual(player_2.element, self.players_tuple[1])
        self.assertEqual(player_3.element, self.players_tuple[2])

    def test_out_of_range_index(self) -> None:
        player: str | None = self.players.get_element_at(7)
        self.assertIsNone(player)
    
    def test_empty_list(self) -> None:
        player: str | None = self.players_empty.get_element_at(0)
        self.assertIsNone(player)
        
    


class TestPush(unittest.TestCase):
    def setUp(self) -> None:
        self.names_tuple: tuple = ('John', 'Jack', 'Ryan')
        self.names: LinkedList = LinkedList()

    def test_adding_when_empty(self) -> None:
        self.names.push(self.names_tuple[0])
        self.assertEqual(self.names.get_element_at(0).element, self.names_tuple[0])
            

    def test_adding_normaly(self) -> None:
        for name in self.names_tuple:
            self.names.push(name)
        
        for i, name in enumerate(self.names_tuple):
            self.assertEqual(self.names.get_element_at(i).element, self.names_tuple[i])

class TestIndexOf(unittest.TestCase):
    def setUp(self) -> None:
        self.players_tuple: tuple = ('Isagi', 'Bachira', 'Nagi')
        self.players: LinkedList = LinkedList()
        self.players_empty: LinkedList = LinkedList()

        for player in self.players_tuple:
            self.players.push(player)
    
    
    def test_search_normaly(self) -> None:
        for i, player in enumerate(self.players_tuple):
            self.assertEqual(self.players.index_of(player), i)

    def test_search_not_in_list(self) -> None:
        self.assertEqual(self.players.index_of('Barou'), -1)

    def test_search_when_empty(self) -> None:
        self.assertEqual(self.players_empty.index_of('Isagi'), -1)

class TestRemoveAt(unittest.TestCase):
    def setUp(self) -> None:
        self.players_tuple: tuple = ('Isagi', 'Bachira', 'Nagi')
        self.players: LinkedList = LinkedList()
        self.players_empty: LinkedList = LinkedList()

        for player in self.players_tuple:
            self.players.push(player)
        
    def test_removing_from_first_position(self) -> None:
        removed_player: any | None = self.players.remove_at(0)

        self.assertEqual(removed_player, self.players_tuple[0])
        self.assertEqual(self.players._count, 2)
        self.assertEqual(self.players.index_of(self.players_tuple[0]), -1)
    
    def test_removing_from_last_position(self) -> None:
        removed_player: any | None = self.players.remove_at(2)
        self.assertEqual(removed_player, self.players_tuple[2])
        self.assertEqual(self.players._count, 2)
        self.assertEqual(self.players.index_of(self.players_tuple[2]), -1)

    def test_removing_from_middle(self) -> None:
        removed_player: any | None = self.players.remove_at(1)
        self.assertEqual(removed_player, self.players_tuple[1])
        self.assertEqual(self.players._count, 2)
        self.assertEqual(self.players.index_of(self.players_tuple[1]), -1)

    def test_removing_inexistent_element(self) -> None:
        removed_player: any | None = self.players.remove_at(10)
        self.assertIsNone(removed_player)

    def test_removing_from_empty_list(self) -> None:
        removed_player: any | None = self.players_empty.remove_at(0)
        self.assertIsNone(removed_player)


class TestRemove(unittest.TestCase):
    def setUp(self) -> None:
        self.players_tuple: tuple = ('Isagi', 'Bachira', 'Nagi')
        self.players: LinkedList = LinkedList()
        self.players_empty: LinkedList = LinkedList()

        for player in self.players_tuple:
            self.players.push(player)
    
    def test_removing_from_first_position(self) -> None:
        removed_player: any | None = self.players.remove(self.players_tuple[0])
        self.assertEqual(removed_player, self.players_tuple[0])
        self.assertEqual(self.players._count, 2)
        self.assertEqual(self.players.index_of(self.players_tuple[0]), -1)
    
    def test_removing_from_last_position(self) -> None:
        removed_player: any | None = self.players.remove(self.players_tuple[2])
        self.assertEqual(removed_player, self.players_tuple[2])
        self.assertEqual(self.players._count, 2)
        self.assertEqual(self.players.index_of(self.players_tuple[2]), -1)

    def test_removing_from_middle(self) -> None:
        removed_player: any | None = self.players.remove(self.players_tuple[1])
        self.assertEqual(removed_player, self.players_tuple[1])
        self.assertEqual(self.players._count, 2)
        self.assertEqual(self.players.index_of(self.players_tuple[1]), -1)

    def test_removing_inexistent_element(self) -> None:
        removed_player: any | None = self.players.remove('Chigiri')
        self.assertIsNone(removed_player)

    def test_removing_from_empty_list(self) -> None:
        removed_player: any | None = self.players_empty.remove('Isagi')
        self.assertIsNone(removed_player)

class TestInsert(unittest.TestCase):
    def setUp(self) -> None:
        self.players: tuple = ('Isagi', 'Nagi', 'Barou')
        self.players_list: LinkedList = LinkedList()

    def test_insert_while_empty(self) -> None:
        players: tuple = self.players
        players_list: LinkedList = self.players_list

        self.assertTrue(players_list.insert(players[0], 0))

        self.assertEqual(players_list._head.element, players[0])
    
    def test_insert_first_position_while_not_empty(self) -> None:
        players: tuple = self.players
        players_list: LinkedList = self.players_list

        players_list.insert(players[0], 0)
        players_list.insert(players[1], 0)


        self.assertEqual(players_list._head.element, players[1])
        self.assertEqual(players_list._head.next.element, players[0])

    def test_insert_last_position(self) -> None:
        players: tuple = self.players
        players_list: LinkedList = self.players_list

        for index, player in enumerate(players):
            self.assertTrue(players_list.insert(player, index))
        
        self.assertEqual(players_list.get_element_at(1).element, players[1])
        self.assertEqual(players_list.get_element_at(2).element, players[2])
    
    def test_insert_middle(self) -> None:
        players: tuple = self.players
        players_list: LinkedList = self.players_list

        self.assertTrue(players_list.insert(players[0], 0))
        self.assertTrue(players_list.insert(players[2], 1))
        self.assertTrue(players_list.insert(players[1], 1))     

        self.assertEqual(players_list.get_element_at(1).element, players[1])
        self.assertEqual(players_list.get_element_at(2).element, players[2])
    
    def test_inserting_index_out_of_range(self) -> None:
        players: tuple = self.players
        players_list: LinkedList = self.players_list
        self.assertFalse(players_list.insert(players[2], 10))
        
