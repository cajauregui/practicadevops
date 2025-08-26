import unittest
import os

class TestHTML(unittest.TestCase):
    def test_index_exists(self):
        self.assertTrue(os.path.isfile("index.html"))

if __name__ == '__main__':
    unittest.main()
