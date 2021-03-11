import unittest

def add(x, y):
    return (x + y)

def sub(x, y):
    return (x - y)

def mult(x, y):
    return (x * y)

def div(x, y):
    return (x / y)


class TestCalc(unittest.TestCase):
    def addTest(self):
        self.assertEqual(add(3,4), 7)
    def subTest(self):
        self.assertEqual(sub(7,1), 6)
    def multTest(self):
        self.assertEqual(mult(3,6), 18)
    def divTest(self):
        self.assertEqual(div(25,5), 5)



if __name__ == '__main__':
    unittest.main()