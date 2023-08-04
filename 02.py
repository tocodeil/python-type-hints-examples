from typing import Any, TypedDict, NotRequired, Literal, Optional
def longer_than(min_len: int, items: list[str]) -> list[str]:
    return [i for i in items if len(i) > min_len]


longer_than(5, ['a', 'b', 'abcdefg', 'hello world'])
longer_than(5, ['a', 'b', 'abcdefg'])


items: list[str | int | bool] = [10, 20, 'abc', False, 30]

#######################


def sum_square_values(d: dict[Any, int]) -> int:
    return sum([x * x for x in d.values()])


print(sum_square_values({'a': 10, 'b': 20}))
print(sum_square_values({'a': 10, False: 20}))


#################


class Point(TypedDict):
    x: int
    y: int
    color: NotRequired[Literal['red', 'blue', 'green', 'yellow', 'white']]


p: Point = {'x': 10, 'y': 20}
q: Point = {'x': 10, 'y': 20}

def distance(p: Point, q: Point):
    pass

z: Point = {'x': 1, 'y': 2, 'color': 'red'}
