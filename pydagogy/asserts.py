from functools import wraps
from . utils import text_format

__all__ = ["assert_equal", "assert_not_equal", "assert_close"]


def assert_func(func):
    
    varnames = func.__code__.co_varnames
    try:
        message_idx = varnames.index("message")
    except ValueError as e:
        raise Exception("Wrapped assert function must have a keyword argument 'message'") from e
    
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
def assert_equal(val1, val2, message=None):
    """ Test docstring """
    if val1 != val2:
        return False
    return True

@assert_func
def assert_not_equal(val1, val2, message=None):
    if val1 == val2:
        return False
    
    return True

@assert_func
def assert_close(val1, val2, tol=1e-3, message=None):
    if abs(val1 - val2) > tol:
        return False
    
    return True