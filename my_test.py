import unittest

class Captcha(object):
    def __init__(self, patter, left, operator, right):
        self.left = left
        self.right = right

    def right_operand(self):
        return str(self.right)

    def left_operand(self):
        number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return  number_text[self.left-1]

class FirstPatternLeftOperandShouldBeText(unittest.TestCase):
    FIRST_PATTERN = 1
    DUMMY_RIGHT = 1
    DUMMY_OPERATOR = 1

    def test_leftoperand_should_be_one(self):
        captcha = Captcha(self.FIRST_PATTERN, 1, self.DUMMY_OPERATOR, self.DUMMY_RIGHT)
        self.assertEqual("one", captcha.left_operand())

    def test_leftoperand_should_be_two(self):
        captcha = Captcha(self.FIRST_PATTERN, 2, self.DUMMY_OPERATOR, self.DUMMY_RIGHT)
        self.assertEqual("two", captcha.left_operand())

    def test_leftoperand_should_be_nine(self):
        captcha = Captcha(self.FIRST_PATTERN, 9, self.DUMMY_OPERATOR, self.DUMMY_RIGHT)
        self.assertEqual("nine", captcha.left_operand())


class FirstPatternRightOperandShouldBeNumber(unittest.TestCase):
    FIRST_PATTERN = 1
    DUMMY_LEFT = 1
    DUMMY_OPERATOR = 1

    def test_right_operand_should_be_1(self):
        captcha = Captcha(self.FIRST_PATTERN, self.DUMMY_LEFT, self.DUMMY_OPERATOR, 1)
        self.assertEqual("1", captcha.right_operand())

    def test_right_operand_should_be_9(self):
        captcha = Captcha(self.FIRST_PATTERN, self.DUMMY_LEFT, self.DUMMY_OPERATOR, 9)
        self.assertEqual("9", captcha.right_operand())
if __name__ == "__main__":
    unittest.main()
