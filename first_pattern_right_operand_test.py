import unittest
from captcha import Captcha

FIRST_PATTERN = 1
DUMMY_LEFT = 1
DUMMY_OPERATOR = 1

class FirstPatternRightOperandShouldBeNumber(unittest.TestCase):
    def test_right_operand_should_be_1(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, DUMMY_OPERATOR, 1)
        self.assertEqual("1", captcha.right_operand())

    def test_right_operand_should_be_9(self):
        captcha = Captcha(FIRST_PATTERN, DUMMY_LEFT, DUMMY_OPERATOR, 9)
        self.assertEqual("9", captcha.right_operand())
