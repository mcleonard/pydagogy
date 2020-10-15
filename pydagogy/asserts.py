from typing import Any, Union, Text
from functools import wraps
from .utils import text_format

Numeric = Union[int, float]

__all__ = ["assert_equal", "assert_not_equal", "assert_close"]


# Assert functions are convenient methods for comparing objects and returning messages
# for failed comparisons. All assert functions must include a keyword argument 'message'
# and return a boolean. Wrap your assert function with the @assert_func decorator to
# get automated printing of the fail message.

def assert_func(func):

    varnames = func.__code__.co_varnames
    try:
        message_idx = varnames.index("message")
    except ValueError as e:
        raise Exception(
            "Wrapped assert function must have a keyword argument 'message'"
        ) from e

    @wraps(func)
    def out_func(*args, **kwargs):

        if "message" in kwargs:
            message = kwargs["message"]
        elif len(args) > message_idx:
            message = args[message_idx]
        else:
            message = ""

        fail_message = text_format("Test failed: ", "red", "bold")

        if message is not None:
            fail_message = fail_message + message

        result = func(*args, **kwargs)

        if not result:
            print(fail_message)

        return result

    return out_func


@assert_func
def assert_equal(val1: Any, val2: Any, message: Text = None) -> bool:
    """ Assert that val1 and val2 are equal. This is valid for any two objects
        that implement equality comparisons.
    """
    if val1 != val2:
        return False
    return True


@assert_func
def assert_not_equal(val1: Any, val2: Any, message: Text=None) -> bool:
    if val1 == val2:
        return False
    return True


@assert_func
def assert_close(val1: Numeric, val2: Numeric, tol: Numeric=1e-3, message: Text=None) -> bool:
    if abs(val1 - val2) > tol:
        return False
    return True


@assert_func
def assert_true(condition: bool, message: Text=None) -> bool:
    return condition


@assert_func
def assert_false(condition: bool, message: Text=None) -> bool:
    return not condition