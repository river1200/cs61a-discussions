def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """

    def cond(i):
        k = 1
        while k <= n:
            if i(k):
                print(k)
            k += 1

    return cond


make_keeper(5)(lambda x: x % 2 == 0)


def f1():
    """
    >>> f1()
    3
    """
    return 3


def f2():
    """
    >>> f2()()
    3
    """
    return lambda: 3


def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: x


def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda: lambda x: lambda: x


print(f1())
print(f2()())
print(f3()(3))
print(f4()()(3)())
