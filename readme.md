# Type Hints In Python

## 1. Basic Type Hints
- [x] What and Why
  https://peps.python.org/pep-3107/
  https://peps.python.org/pep-0484/

- [x] Life without types

- [x] Type Hints: Mypy, pycharm, VS Code

- [x] Type Hints are available in runtime (`inspect.get_annotations`)

## 2. Generic Types
- [x] Generic lists
  - list[int], list[str], list[int|str|bool]

- [x] Generic Dictionaries
  - dict[str, int], dict[Any, int]

- [x] TypedDict
  - use only specific keys in dict
  - Literal
  - NotRequired

## 3. Types & Functions

- [x] Simple input/output type hints
  def x(a: str, b: int) -> list[int]:
    pass

- [x] Typing *args

- [x] Typing **kwargs

- [x] Default args

- [x] Generator Functions

- [x] Warning: Type Hints and Built-in functions

## 4. Types And Object Oriented Programming

- [x] Every class is a type

- [x] Protocols

- [x] Type Hints for Recursive Structures

class Node:
  value: int
  left: Node
  right: Node
  
  def dfs():
    pass

n = Node(10)
n.right = Node(12)
n.right.right = Node(15)
n.right.left = Node(9)
n.dfs()


## 5. Type Vars

- [x] Unsolved Identity Problem

- [x] Hello TypeVar

- [x] Hello ParamSpec

- [x] Types for Decorators


## 6. User Defined Type Guards

- [x] Built-in Type Guards

- [x] Creating Your Own Type Guard

- [x] casting


## 7. NewType and Type Aliases
- [x] Creating type aliases

- [x] Defining new types with NewType 
