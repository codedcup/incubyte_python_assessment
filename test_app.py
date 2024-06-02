import unittest
from app import add;

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)
        
    def test_one_number(self):
        self.assertEqual(add("1"), 1)
        
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
        
    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)
        
    def test_new_lines_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)

if __name__ == "__main__":
    unittest.main()