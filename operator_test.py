import unittest
from captcha import Captcha

FIRST_PATTERN = 1
DUMMY_LEFT = 1
DUMMY_RIGHT = 1
DUMMY_OPERATOR = 1
class OperatorTest(unittest.TestCase):
    def test_should_be_plus(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, 1, DUMMY_RIGHT)
        self.assertEqual("+", captcha.oper())

    def test_should_be_multiply(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, 2, DUMMY_RIGHT)
        self.assertEqual("*", captcha.oper())

    def test_should_be_minus(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, 3, DUMMY_RIGHT)
        self.assertEqual("-", captcha.oper())
