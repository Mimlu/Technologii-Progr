from behave import given, when, then
from divide import divide

@given('I have a number {number:d}')
def step_given_number(context, number):
    context.number = number

@given('I have a divisor {divisor:d}')
def step_given_divisor(context, divisor):
    context.divisor = divisor

@when('I divide the number by the divisor')
def step_when_divide(context):
    context.result = divide(context.number, context.divisor)

@then('the result should be {expected_result:f}')
def step_then_result(context, expected_result):
    assert context.result == expected_result

@then('an error should be raised')
def step_then_error(context):
    try:
        divide(context.number, context.divisor)
        assert False, "Expected ValueError was not raised"
    except ValueError:
        pass
