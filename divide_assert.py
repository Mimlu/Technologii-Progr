def divide(a, b):
    assert b != 0, 'нельзя делить на 0'

    return round(a/b, 2)

x = divide(21, 0)
print(x)