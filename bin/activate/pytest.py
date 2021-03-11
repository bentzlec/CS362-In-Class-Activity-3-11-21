import unittest
import calc

class TestCalc(unittest.TestCase):
   def test_1(self):
      self.assertEqual(calc.add(10, 10), 20)
