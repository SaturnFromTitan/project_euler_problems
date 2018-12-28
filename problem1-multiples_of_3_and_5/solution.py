from utils import timeit


@timeit
def sum_of_multiples_of_3_or_5(below: int) -> int:
    return sum(n for n in range(1, below) if is_multiple_of_3(n) or is_multiple_of_5(n))


def is_multiple_of_3(number: int) -> bool:
    return _is_multiple_of(number, 3)


def is_multiple_of_5(number: int) -> bool:
    return _is_multiple_of(number, 5)


def _is_multiple_of(number: int, n: int) -> bool:
    return (number % n) == 0


if __name__ == '__main__':
    result = sum_of_multiples_of_3_or_5(below=1000)
    print(result)
