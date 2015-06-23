import unittest
from captcha import Captcha

FIRST_PATTERN = 1
SECOND_PATTERN = 2
DUMMY_RIGHT = 1
DUMMY_LEFT = 1
DUMMY_OPERATOR = 1

class SecondPatternLeftOperandShouldBeNumber(unittest.TestCase):
    def test_left_operand_should_be_1(self):
        captcha = Captcha(SECOND_PATTERN, 1, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("1", captcha.left_operand())

    def test_left_operand_should_be_9(self):
        captcha = Captcha(SECOND_PATTERN, 9, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("9", captcha.left_operand())

class SecondPatternRightOperandShouldBeString(unittest.TestCase):
    def test_right_operand_should_be_one(self):
        captcha = Captcha(SECOND_PATTERN, DUMMY_LEFT, DUMMY_OPERATOR, 1)
        self.assertEqual("one", captcha.right_operand())

    def test_right_operand_should_be_nine(self):
        captcha = Captcha(SECOND_PATTERN, DUMMY_LEFT, DUMMY_OPERATOR, 9)
        self.assertEqual("nine", captcha.right_operand())
