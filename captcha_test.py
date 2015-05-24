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

#    def test_left_operand_should_be_9(self):
#        captcha = Captcha(SECOND_PATTERN, 9, DUMMY_OPERATOR, DUMMY_RIGHT)
#        self.assertEqual("9", captcha.left_operand())

class FirstPatternLeftOperandShouldBeText(unittest.TestCase):
    def test_leftoperand_should_be_one(self):
        captcha = Captcha(FIRST_PATTERN, 1, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("one", captcha.left_operand())

    def test_leftoperand_should_be_two(self):
        captcha = Captcha(FIRST_PATTERN, 2, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("two", captcha.left_operand())

    def test_leftoperand_should_be_nine(self):
        captcha = Captcha(FIRST_PATTERN, 9, DUMMY_OPERATOR, DUMMY_RIGHT)
        self.assertEqual("nine", captcha.left_operand())
