#!/usr/bin/python3
"""A function that calculate factorial"""


def factorial(n: int) -> int:

    return_value = 1 if n <= 1 else n * factorial(n-1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value


if __name__ == '__main__':

    print(factorial.__annotations__)
    factorial(0)
    print("-------------------------------------")
    factorial(4)
