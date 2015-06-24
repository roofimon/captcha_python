import unittest
from captcha import Captcha

FIRST_PATTERN = 1
DUMMY_LEFT = 1
DUMMY_RIGHT = 1
DUMMY_OPERATOR = 1
class FirstPattern(unittest.TestCase):
    def test_string_should_be_one_plus_1(self):
        captcha = Captcha(1, 1, 1, 1)
        self.assertEqual("one + 1", captcha.string())
    def test_string_should_be_one_plus_9(self):
        captcha = Captcha(1, 1, 1, 9)
        self.assertEqual("one + 9", captcha.string())

class FirstPatternLeftOperandShouldBeString(unittest.TestCase):
    def test_left_operand_should_be_one(self):
        captcha = Captcha(FIRST_PATTERN, 1, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("one", captcha.left_operand())
    def test_left_operand_should_be_nine(self):
        captcha = Captcha(FIRST_PATTERN, 9, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("nine", captcha.left_operand())

class FirstPatternRightOperandShouldBeNumber(unittest.TestCase):
    def test_right_operand_should_be_1(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, DUMMY_OPERATOR, 1)
        self.assertEqual("1", captcha.right_operand())

    def test_right_operand_should_be_9(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, DUMMY_OPERATOR, 9)
        self.assertEqual("9", captcha.right_operand())
