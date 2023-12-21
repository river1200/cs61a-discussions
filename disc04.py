def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total


def even_weighted_loop(s):
    """Takes a list s and returns a new list composed of only the even-indexed elements of s and multiplied them by their corresponding index
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    even_weighted_list = []
    for x in range(len(s)):
        if not x % 2:
            even_weighted_list += [(s[x] * x)]
    return even_weighted_list


def even_weighted_comprehension(s):
    """Takes a list s and returns a new list composed of only the even-indexed elements of s and multiplied them by their corresponding index
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_comprehension(x)
    [0, 6, 20]
    """
    return [s[x] * x for x in range(len(s)) if not x % 2]


def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        with_first = s[0] * max_product(s[2:])
        if len(s) > 1:
            with_second = s[1] * max_product(s[3:])
        else:
            with_second = 0
    return max(with_first, with_second)
