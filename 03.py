# from collections.abc import Generator
from typing import Optional, Generator
from itertools import islice
def longer_than(min_len: int, *items: str) -> list[str]:
    return [i for i in items if len(i) > min_len]


def count_sentence(text: str, **kwargs: int) -> int:
    return sum(kwargs.get(w, 0) for w in text.split())


print(longer_than(3, 'ab', 'abc', 'abcd', 'wow'))
print(count_sentence('I can see a rainbow and a car', can=2, a=10, rainbow=30))
print(count_sentence('I can see a rainbow and a car', can=9, a=10, rainbow=30))


def write_times(text: str, times: Optional[int] = None):
    if times is None:
        return 7

    for i in range(times):
        print(text)



def even() -> Generator[int, None, None]:
    i = 0
    while True:
        yield i
        i += 2


print(list(islice(even(), 10))[0])

import pickle

# x = pickle.loads(pickle.dumps({}))
# reveal_locals()
# print(x + 1)









