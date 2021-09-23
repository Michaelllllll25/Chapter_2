#### ANNOTATIONS


# Takes two ints and returns an int
def add(a: int, b: int) -> int:                                   # a and b are parameters ///// -> means what it will return
    return a + b                                                  # function is now annotated

# Takes a string and returns an int
def string_length(my_string: str) -> int:
    return len(my_string)

def average(a: float, b: float) -> float:                            # since division it will return a float // a and b don't need to be float
    return (a + b) / 2

# Takes a list of integers and returns an int
def sum_list(numbers: list[int]) -> int:                            # [] specifies whats in the list
    total = 0
    for n in numbers:
        total += n
    return total 



"""
from typing import

some_integer: int
some_string: str
some_float: float
list_of_integers: list[int]
tuple_with_an_int_and_a_string: tuple[int, str]        # tuple first position is always an int, follwed by a string
two_dimensional_list_of_integers: list[list[int]]      # list that contains a list of integers
either_an_integer_or_none: optional[int] = None        # indicates that it takes an int but it is okay if you don't give it one

"""
