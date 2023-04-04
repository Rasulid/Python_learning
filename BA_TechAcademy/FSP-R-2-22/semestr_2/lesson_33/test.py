import unittest
import lesson_33
import homework

class Testlesson33(unittest.TestCase):
    def test_do_staff(self):
        num = 5
        result = lesson_33.do_staff(num)
        self.assertEqual(result , 15)

    def test_do_staff_2(self):
        num = '10'
        result = lesson_33.do_staff(num)
        self.assertEqual(result,20)

    def test_do_staff_3(self):
        num = 40
        result = lesson_33.do_staff(num)
        self.assertEqual(result, 50)




