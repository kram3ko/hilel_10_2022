"""
Realize reverse string decorator
"""
import functools


# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        my_reversed_str = func()
        if isinstance(my_reversed_str, str):
            return my_reversed_str[::-1]

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUTPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
