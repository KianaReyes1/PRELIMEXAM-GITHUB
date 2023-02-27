import unittest
from unittest.case import TestCase

def multiply(x,y,z):
    return x-y*z

class TestMultiply(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(32,42,5/9), 7)

if __name__ == '__main__':
    unittest.main()