from functools import wraps
from time import time
from typing import Callable
import sys
import inspect


class Logging:
    """
    decorator class for logging a function by a template,
    with substitution of the function's running time.
    """

    def __init__(self, sample: str):
        self.sample = sample

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper() -> None:
            t0 = time()
            try:
                return func()
            finally:
                t1 = time()
                print(self.sample.format(int(t1 - t0)))

        return wrapper


def get_classes_from_module(module_name: str) -> list:
    return list(
        dict(
            inspect.getmembers(
                sys.modules[module_name],
                lambda member: inspect.isclass(member)
                and member.__module__ == module_name,
            )
        ).values()
    )
