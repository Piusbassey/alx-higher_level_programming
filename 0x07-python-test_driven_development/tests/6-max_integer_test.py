import unittest
from main import max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_max_integer(self):
        """Test the normal cases"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([3, 5, 2]), 5)

    def test_empty_list(self):
        """Test the empty list case"""
        self.assertIsNone(max_integer([]))

    def test_invalid_input(self):
        """Test the invalid input cases"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [1, 2, "3"])
        self.assertRaises(TypeError, max_integer, 5)
