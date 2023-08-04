from typing import Any, TypeGuard, Literal, cast
import os
import random

secret = os.environ.get('SECRET')


# Type Guard
if secret is not None:
    # secret is a str
    print(f"My secret is {secret.capitalize()}")
else:
    # secret is None
    print(f"I have no secret")


l = [random.choice([7, 'seven']) for _ in range(3)]


# User defined type guard
def all_are_seven(l: list[Any]) -> TypeGuard[list[Literal['seven']]]:
    return all([w == 'seven' for w in l])


if all_are_seven(l):
    print(l[0].capitalize())
    print('Bravo!')
else:
    pass


if any([w == 'seven' for w in l]):
    print("there are sevens in the list")
else:
    casted_list = cast(list[Literal[7]], l)
    print(casted_list[0] + 5)




