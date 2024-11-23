from behave import *
from bubble_sort import bubble_sort

@given('список чисел: {list}')
def step_impl(context, list):
    context.input_list = eval(list) #Используем eval для преобразования строки в список

@when('я сортирую список пузырьком')
def step_impl(context):
    context.output_list = bubble_sort(context.input_list)

@then('отсортированный список должен быть: {sorted_list}')
def step_impl(context, sorted_list):
    assert context.output_list == eval(sorted_list)