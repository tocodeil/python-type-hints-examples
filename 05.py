from typing import Sized, TypeVar, Callable, ParamSpec


LongerThanRT = TypeVar('LongerThanRT', str, list, Sized)
def longer_than(min_len: int, *items: LongerThanRT) -> list[LongerThanRT]:
    return [i for i in items if len(i) > min_len]


x = longer_than(3, [1, 2, 3], [10, 20, 30, 40], [99, 99, 99, 99, 99, 99])
y = longer_than(3, 'ab', 'abc', 'abcd', 'wow')
z = longer_than(3, 'ab', [1, 2, 3, 4], 'abc', 'abcd', 'wow')

print(y[0].capitalize())

P = ParamSpec('P')
R = TypeVar('R')


def logged(f: Callable[P, R]) -> Callable[P, R]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Function {f.__name__} was called with {args} and {kwargs}")
        return f(*args, **kwargs)
    return inner


@logged
def twice(x: int) -> int:
    return x * 2


twenty = twice(10)
print(twenty.capitalize())











