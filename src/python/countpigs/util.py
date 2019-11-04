from functools import wraps


def memoize(func):
    _registry_ = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (*args, *tuple(kwargs.items()))
        if key not in _registry_:
            _registry_[key] = func(*args, **kwargs)
        return _registry_[key]
    return wrapper
