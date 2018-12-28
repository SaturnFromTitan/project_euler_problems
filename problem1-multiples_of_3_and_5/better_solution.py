"""
In the naive solution we created a generator of all numbers in question, looped over them and checked whether
they are divisible by 3 or 5, respectively.

There's a better approach to this! Instead of checking all numbers 1000 numbers if they are divisible by 3 or 5,
rather only construct the numbers being divisible by 3 or 5, merge them and sum over them.
"""
from utils import timeit


@timeit
def sum_of_multiples_of_3_or_5(until: int) -> int:
    multiples_of_3 = _multiples_of_n(3, until)
    multiples_of_5 = _multiples_of_n(5, until)
    multiples_of_3_or_5 = multiples_of_3 | multiples_of_5
    return sum(multiples_of_3_or_5)


def _multiples_of_n(n: int, until: int) -> set:
    return set(range(0, until, n))


if __name__ == '__main__':
    result = sum_of_multiples_of_3_or_5(until=1000)
    print(result)
