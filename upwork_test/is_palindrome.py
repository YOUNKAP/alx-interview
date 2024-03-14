#!/usr/bin/python3
"""A function that calculate factorial"""


def is_palindrome(word: str) -> bool:
    """Return True if word is a palindrome, False if not."""

    print(word)
    if (word == word[::-1]):
        return True
    else:
        return False


if __name__ == '__main__':

    print(is_palindrome.__annotations__)
    pal = is_palindrome("foo")
    print(pal)
    print("-------------------------------------")
    pal = is_palindrome("racecar")
    print(pal)
    print("-------------------------------------")
    pal = is_palindrome("troglodyte")
    print(pal)
    print("-------------------------------------")
    pal = is_palindrome("civic")
    print(pal)
