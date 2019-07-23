from typing import List
import random
from random import randint

def list_random_numbers(min: int, max: int, length: int) -> List:
    """ Return a list of random number between min and max. The list will count `length`
    items.
    :param int min: the lower number that can be added
    :param int max: the highest number that can be added
    :param int length: the number of items that will be in the list
    :rtype: list
    """
    # Many instructions + test condition we can use random.sample()
    # See next function 'list_random_sample_numbers()'
    result = []
    while len(result) < length:
        n = randint(min, max)
        if n not in result:
            result.append(n)
    return result

def list_random_sample_numbers(min: int, max: int, length: int) -> List:
    """ Return a list of random number between min and max. The list will count `length`
    items.
    :param int min: the lower number that can be added
    :param int max: the highest number that can be added
    :param int length: the number of items that will be in the list
    :rtype: list
    """
    result = random.sample(range(min, max), length)
    return result


if __name__ == "__main__":
    res = list_random_numbers(5, 1000000000, 3)
    print(res)

    res = list_random_sample_numbers(5, 1000000000, 3)
    print(res)
