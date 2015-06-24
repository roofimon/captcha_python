class Captcha(object):
    number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    operation_text = ["+", "*", "-"]

    def __init__(self, pattern, left, operator, right):
        self.operator = operator
        self.pattern = pattern
        self.left = left
        self.right = right

    def string(self):
        return "%s %s %s" % (self.left_operand(), self.operation(), self.right_operand())

    def operation(self):
        return self.operation_text[self.operator - 1]

    def right_operand(self):
        if self.is_number_operation_string_pattern():
            right = self.number_text[self.right - 1]
        else:
            right = str(self.right)
        return right

    def is_number_operation_string_pattern(self):
        return self.pattern == 2

    def left_operand(self):
        if self.pattern == 1:
            left = self.number_text[self.left - 1]
        else:
            left = str(self.left)
        return left
