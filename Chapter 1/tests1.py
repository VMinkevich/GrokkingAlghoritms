import unittest
import BinSearch as bs

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 5
        expected = 4
        self.assertEqual(bs.binSearch(arr, target), expected)

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10
        expected = -1
        self.assertEqual(bs.binSearch(arr, target), expected)

    def test_empty_array(self):
        arr = []
        target = 1
        expected = -1
        self.assertEqual(bs.binSearch(arr, target), expected)

    def test_single_element_found(self):
        arr = [1]
        target = 1
        expected = 0
        self.assertEqual(bs.binSearch(arr, target), expected)

    def test_single_element_not_found(self):
        arr = [1]
        target = 2
        expected = -1
        self.assertEqual(bs.binSearch(arr, target), expected)

if __name__ == '__main__':
    unittest.main()
