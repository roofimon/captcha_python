class Captcha(object):
    number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    oper_text = ["+", "*", "-"]
    def __init__(self, pattern, left, operator, right):
        self.operator = operator
        self.pattern = pattern
        self.left = left
        self.right = right
    
    def oper(self):
        return self.oper_text[self.operator-1] 

    def right_operand(self):
        if self.pattern == 2:
            return self.number_text[self.right-1] 
        return str(self.right)

    def left_operand(self):
        if self.pattern == 1 :  
            left = self.number_text[self.left-1]
        else:
            left = str(self.left) 
        return left
