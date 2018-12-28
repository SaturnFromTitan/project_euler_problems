from utils import timeit


@timeit
def sum_of_even_fibonacci_numbers(until: int) -> int:
    a = 1
    b = 2
    fibonaccis = [a, b]

    while b < until:
        a, b = b, a + b
        fibonaccis.append(b)

    # With a little bit of thinking it's clear that starting from the second number, every third number in the sequence
    # is going to be even and the others must be odd
    #
    # It's easy to see that when you understand that the sum of two odd numbers is even and the sum of an odd and an
    # even number must be odd again.
    even_fibonaccis = fibonaccis[1::3]
    return sum(even_fibonaccis)


if __name__ == '__main__':
    one_million = 10**6
    result = sum_of_even_fibonacci_numbers(until=4*one_million)
    print(result)
