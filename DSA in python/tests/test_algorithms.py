import unittest
from algorithms.binary_search import binary_search, search_in_array

class TestBinarySearch(unittest.TestCase):

    def test_target_found(self):
        """Test when the target is found in the array."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_target_not_found(self):
        """Test when the target is not found in the array."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_target_at_start(self):
        """Test when the target is at the start of the array."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_target_at_end(self):
        """Test when the target is at the end of the array."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_empty_array(self):
        """Test when the array is empty."""
        self.assertEqual(binary_search([], 1), -1)

    def test_negative_numbers(self):
        """Test when the array contains negative numbers."""
        self.assertEqual(binary_search([-5, -3, -1, 0, 2, 4], -3), 1)

    def test_search_in_array_found(self):
        """Test the search_in_array function when the target is found."""
        result = search_in_array([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 'Target 3 found at index: 2')

    def test_search_in_array_not_found(self):
        """Test the search_in_array function when the target is not found."""
        result = search_in_array([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, 'Target 6 not found in the array.')

if __name__ == "__main__":
    unittest.main()
