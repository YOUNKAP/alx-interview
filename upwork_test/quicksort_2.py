#!/usr/bin/python3
"""A function that calculate factorial"""


import statistics


def quicksort(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )

        return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
        )


if __name__ == '__main__':

    import random

    def get_random_numbers(length, minimum=1, maximum=100):
        numbers = []
        for i in range(length):
            numbers.append(random.randint(minimum, maximum))
            
        return numbers
    numbers = get_random_numbers(20)
    print(numbers)
    print(quicksort(numbers))
