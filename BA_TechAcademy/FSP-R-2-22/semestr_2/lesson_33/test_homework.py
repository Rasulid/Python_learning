import unittest
import homework


class TestRandom(unittest.TestCase):
    def test_rondom_int(self):
        num1 = 0
        num2 = 10
        result = homework.rondom_int(num1,num2)
        self.assertEqual(result )



#https://docs.python.org/3/library/unittest.html#organizing-tests