class Captcha(object):
    def __init__(self, patter, left, operator, right):
        self.left = left
        self.right = right

    def right_operand(self):
        return str(self.right)

    def left_operand(self):
        number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return  number_text[self.left-1]
