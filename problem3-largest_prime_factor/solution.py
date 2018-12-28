import math
import logging
from utils import timeit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@timeit
def largest_prime_factor(number: int) -> int:
    logger.info("Checking if number is prime.")
    if is_prime(number):
        logger.info("number is prime.")
        return number
    logger.info("number is not prime.")

    upper_bound = math.ceil(number / 2)
    for factor in range(2, upper_bound + 1):
        if is_prime(factor):
            logger.info(f"Checking prime number {factor}.")
            while is_divisor(number, factor):
                number /= factor
                if number == 1:
                    return factor


def is_prime(number):
    upper_bound = math.ceil(math.sqrt(number))
    for factor in range(2, upper_bound + 1):
        if is_divisor(number, factor) and number != factor:
            # number != factor so that 2 is correctly flagged as prime
            return False
    return True


def is_divisor(number, factor):
    return number % factor == 0


if __name__ == '__main__':
    result = largest_prime_factor(number=600851475143)
    print(result)
