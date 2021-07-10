import time

from url_deco import *
from functools import lru_cache
import math


@lru_cache(10)
def memory_pow(x:int, y:int):
    math.pow(x, y)


if __name__ == "__main__":
    print('Start server deamon to wait for requests.')
    print('When load url_deco module, we expect all the decorated functions are executed.')
    time.sleep(3)
