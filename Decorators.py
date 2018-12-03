import math


def decor_function_for_check(func):
    def inside(a, b):
        if a < 0 or b < 0 or (a+b) == 0:
            return 'a < 0 or b < 0 or (a+b) == 0, fail'
        return func(a, b)
    return inside


@decor_function_for_check
def decored_function(a, b):
    c = math.sqrt(a + b)
    return c


print(decored_function(6, -4))
