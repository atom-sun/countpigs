from .util import memoize
from numpy import array
from scipy.special import comb


@memoize
def binomial(n, k):
    # return comb(n, k, exact=True)  # long integer fail when n >= 15
    return comb(n, k)


@memoize
def f(m, q, k):
    """Counting factor of (m, q, k).

    """
    return array(tuple(fg(m, q, k))).sum()


def fg(m, q, k):
    """The generator for f(m, q, k).

    """
    if k < q or m * q < k:
        yield 0
    elif k == q:
        yield 1
    else:
        for i in range(q+1):
            yield binomial(k-i, q-i) * binomial(k, i) * f(m-1, q, k-i)


@memoize
def p(n, m, q, k):
    """Probability of (n, m, q, k).

    """
    return binomial(n, k) * f(m, q, k) / binomial(n, q) ** m


@memoize
def expect_val(n, m, q):
    """Expectation value of the num `k' of (n, m, q) event.

    """
    return array([k * p(n, m, q, k) for k in range(m*q + 1)]).sum()
