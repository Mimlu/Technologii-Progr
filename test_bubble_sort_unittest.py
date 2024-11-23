import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(bubble_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(bubble_sort([3, 4, 5, 6, 7]), [3, 4, 5, 6, 7])

    def test_unsorted_list(self):
        self.assertEqual(bubble_sort([5, 1, 3, 2, 8]), [1, 2, 3, 5, 8])

    def test_list_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-5, 2, -1, 0, 3]), [-5, -1, 0, 2, 3])


if __name__ == '__main__':
    unittest.main()