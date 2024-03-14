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

    print(quicksort.__annotations__)
    pal = quicksort([])
    print(pal)
    print("-------------------------------------")
    pal = quicksort([42])
    print(pal)
    print("-------------------------------------")
    pal = quicksort([5, 2, 6, 3])
    print(pal)
    print("-------------------------------------")
    pal = quicksort([10, -3, 21, 6, -8])
    print(pal)
