import functools
from utils import timeit


@timeit
def sum_of_multiples_of_3_or_5(below: int) -> int:
    is_multiple_of_3 = functools.partial(_is_multiple_of, n=3)
    is_multiple_of_5 = functools.partial(_is_multiple_of, n=5)
    return sum(n for n in range(1, below) if is_multiple_of_3(n) or is_multiple_of_5(n))


def _is_multiple_of(number: int, n: int) -> bool:
    return (number % n) == 0


if __name__ == '__main__':
    result = sum_of_multiples_of_3_or_5(below=1000)
    print(result)
