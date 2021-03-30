def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if b is None:
        begin = 0
        end = a
        while begin < end:
            yield begin
            begin += 1
    elif c is None:
        begin = a
        end = b
        while begin < end:
            yield begin
            begin += 1
    else:
        begin = a
        end = b
        if begin > end:
            if 0 < c:
                return []
            while begin > end:
                begin += c
                yield begin - c
        else:
            while begin < end:
                if c < 0:
                    return []
                yield begin
                begin += c
