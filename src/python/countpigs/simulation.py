from .util import memoize
import itertools
from numpy import argwhere, array


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
