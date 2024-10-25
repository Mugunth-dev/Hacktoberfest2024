import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Create a linked list for testing."""
        self.linked_list = LinkedList()
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

    def test_append(self):
        """Test appending elements to the linked list."""
        self.linked_list.append(4)
        self.assertEqual(self.linked_list.head.next.next.next.value, 4)

    def test_length_after_append(self):
        """Test the length of the linked list after appending."""
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.head.next.value, 2)
        self.assertEqual(self.linked_list.head.next.next.value, 3)

    def test_reverse(self):
        """Test reversing the linked list."""
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.head.value, 3)
        self.assertEqual(self.linked_list.head.next.value, 2)
        self.assertEqual(self.linked_list.head.next.next.value, 1)

    def test_reverse_empty_list(self):
        """Test reversing an empty linked list."""
        empty_list = LinkedList()
        empty_list.reverse()
        self.assertIsNone(empty_list.head)

    def test_reverse_single_element(self):
        """Test reversing a linked list with a single element."""
        single_element_list = LinkedList()
        single_element_list.append(1)
        single_element_list.reverse()
        self.assertEqual(single_element_list.head.value, 1)

if __name__ == "__main__":
    unittest.main()
