from lettuce import * 
from captcha import Captcha

@step(u'Given initial value pattern is "([^"]*)"')
def given_initial_value_pattern_is_pattern(step, pattern):
    world.pattern = int(pattern)

@step(u'And left is "([^"]*)"')
def and_left_is_left(step, left):
    world.left = int(left)

@step(u'And operand is "([^"]*)"')
def and_operand_is_operand(step, operand):
    world.operator = int(operand)

@step(u'And right is "([^"]*)"')
def and_right_is_right(step, right):
    world.right = int(right)

@step(u'When I want get left operand')
def when_i_want_get_left_operand(step):
    captcha = Captcha(world.pattern, world.left, world.operator, world.right)
    world.actual = captcha.left_operand()

@step(u'Then I will see "([^"]*)"')
def then_i_will_see_expected(step, expected):
    assert world.actual, expected 
