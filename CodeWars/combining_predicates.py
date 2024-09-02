# Hmmmm, how do we go about this...
# You decide!


class predicate:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        return self.fun(*args, **kwargs)

    def __invert__(self):
        @predicate
        def resf(*args, **kwargs):
            return not self.fun(*args, **kwargs)
        return resf

    def __or__(self, other):
        @predicate
        def resf(*args, **kwargs):
            return self.fun(*args, **kwargs) or other.fun(*args, **kwargs)
        return resf

    def __and__(self, other):
        @predicate
        def resf(*args, **kwargs):
            return self.fun(*args, **kwargs) and other.fun(*args, **kwargs)
        return resf


@predicate
def is_equal(a, b):
    return a == b


@predicate
def is_less_than(a, b):
    return a < b


@predicate
def is_even(a):
    return a % 2 == 0


@predicate
def is_positive(a):
    return a > 0

print(is_even(3))
print((is_even & is_positive)(4))
print((is_less_than | is_equal)(2, b=2))    # True
print((~is_less_than | is_equal)(a=3, b=2))  # False
print((~ is_even)(3))