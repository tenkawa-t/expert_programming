def dummy_decorator(function):
    def wrapped(*args, **kwargs):
        """internal wrap docstring"""
        return function(*args, **kwargs)
    return wrapped


@dummy_decorator
def function_with_importand_docstring():
    """important docstring"""


print(function_with_importand_docstring.__name__)
print(function_with_importand_docstring.__doc__)

from functools import wraps
def preserving_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        """internal wrap docstring"""
        return function(*args, **kwargs)
    return wrapped


@preserving_decorator
def function_with_importand_docstring():
    """important docstring"""


print(function_with_importand_docstring.__name__)
print(function_with_importand_docstring.__doc__)
