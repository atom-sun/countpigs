from functools import wraps
import itertools
from numpy import argwhere, array, unique
import time


def memoize(func):
    _registry_ = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (*args, *tuple(kwargs.items()))
        if key not in _registry_:
            _registry_[key] = func(*args, **kwargs)
        return _registry_[key]
    return wrapper


@memoize
class Pig(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{type(self).__name__}({self.name})'


@memoize
class CountPigs(object):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f'{type(self).__name__}({self.n})'

    @memoize
    def zhujuan(self):
        return tuple(map(Pig, range(self.n)))

    @memoize
    def choice(self, q):
        return tuple(itertools.combinations(self.zhujuan(), q))

    @memoize
    def choices(self, q, m):
        return tuple(itertools.product(self.choice(q), repeat=m))

    @memoize
    def choose(self, q, m, k):
        sel = lambda x: len(set(array(x).flatten())) == k
        ixs = tuple(map(sel, self.choices(q, m)))
        return array(self.choices(q, m))[argwhere(ixs).ravel()]


if __name__ == '__main__':
    # (n, q, m, k) = (5, 2, 3, 3)
    t1 = time.time()
    c = CountPigs(5)
    choice = c.choice(2)
    choices = c.choices(2, 3)
    choose = c.choose(2, 3, 3)
    t2 = time.time()
    print(len(choices), len(choose))
    print(f'Running time: {t2-t1:5.2f} sec.')


@memoize
def directcountpigs(n, q, m, k):
    choices_list = itertools.product(itertools.combinations(
        tuple(map(Pig, range(n))), q), repeat=m)
    x0, x1 = 0, 0
    for c in choices_list:
        x0 += 1
        if len(set(array(c).flatten())) == k:
            x1 += 1
    return x0, x1


if __name__ == '__main__':
    # (n, q, m, k) = (5, 2, 3, 3)
    t1 = time.time()
    x0, x1 = directcountpigs(5, 2, 3, 3)
    t2 = time.time()
    print(x0, x1)
    print(f'Running time: {t2-t1:5.2f} sec.')
