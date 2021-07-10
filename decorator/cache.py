import math
from functools import lru_cache


# The first parameter is the cache memory size.
# The second flag is to determine if the cache has to consider the type of the input parameter.
@lru_cache(10, typed=False)
def memory_pow(x: int, y: int):
    res = math.pow(x, y)
    print(f'Calculate: {x} pow {y} = {res}')


if __name__ == "__main__":

    # Calculate the result for the first time.
    memory_pow(2, 5)
    # The second time, the result should come from cache.
    memory_pow(2, 5)
    # Even the type is different, the cache still hits.
    memory_pow(2.0, 5)
