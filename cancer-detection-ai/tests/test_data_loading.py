import unittest
from src.data.load_data import load_data

class TestDataLoading(unittest.TestCase):
    def test_load_data(self):
        data = load_data('test_data.csv')
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()