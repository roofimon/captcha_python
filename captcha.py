class Captcha(object):
    def __init__(self, pattern, left, operator, right):
        self.pattern = pattern
        self.left = left
        self.right = right

    def right_operand(self):
        return str(self.right)

    def left_operand(self):
        number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if self.pattern == 1 :  
            return  number_text[self.left-1]
        return "1"

        
