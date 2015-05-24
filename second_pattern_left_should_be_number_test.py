import unittest
from captcha import Captcha

FIRST_PATTERN = 1
SECOND_PATTERN = 2
DUMMY_RIGHT = 1
DUMMY_OPERATOR = 1

class SecondPatternLeftOperandShouldBeNumber(unittest.TestCase):
    def test_left_operand_should_be_1(self):
        captcha = Captcha(SECOND_PATTERN, 1, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("1", captcha.left_operand())

    def test_left_operand_should_be_9(self):
        captcha = Captcha(SECOND_PATTERN, 9, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("9", captcha.left_operand())
