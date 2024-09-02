class UnexpectedTypeException(Exception):
    pass


def expected_type(types):
    def inner(fun):
        def wrapper(*args, **kwargs):
            res = fun(*args, **kwargs)
            if isinstance(res, (set, list, tuple)):
                rtypes = set(map(type, res))
            else:
                rtypes = {type(res)}

            if not rtypes.intersection(set(types)):
                raise UnexpectedTypeException(r'\(^_^)/')
            return res
        return wrapper
    return inner


@expected_type((str,))
def func(x):
    return type(x)(10)


@expected_type((float,))
def div(x, y):
    return x // y


print(func('kek'))

print(div(4, 2))