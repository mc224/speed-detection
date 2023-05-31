def first_second(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)


def first_fourth(f, x, h):
    return (8*f(x+h) - 8 * f(x-h) - f(x+2*h) + f(x-2*h)) / (12*h)


def second_second(f, x, h):
    return (f(x+h) - 2 * f(x) + f(x-h)) / (h**2)


def second_fourth(f, x, h):
    return (16*f(x+h) - 30*f(x) + 16 * f(x-h) - f(x+2*h) - f(x-2*h)) / (12*h**2)


def fourth_second(f, x, h):
    return (f(x+2*h) + f(x-2*h)+6*f(x)-4*f(x+h)-4*f(x-h)) / (h**4)


def fourth_fourth(f, x, h):
    return (2*f(x+2*h) + 2 * f(x-2*h) - 1/6 * f(x+3*h) - 1/6 * f(x-3*h) - 13/2 * f(x+h) - 13/2*f(x-h) + 28/3 * f(x)) \
           / (h**4)


test_function = lambda x: 9 * (x**3 + 4 * x**4) + 5 * x**5

print(first_second(test_function, 3, 1))
print(first_fourth(test_function, 3, 1))
print(second_second(test_function, 3, 1))
print(second_fourth(test_function, 3, 1))
print(fourth_second(test_function, 3, 1))
print(fourth_fourth(test_function, 3, 1))
