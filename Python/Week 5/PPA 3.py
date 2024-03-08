def maxval(a, b, c):
    """
    compute the maximum among three numbers

    Arguments:
        a, b, c: integers
    Return:
        max_of_three: integer
    """
    if (a > b) and (a > c):
        return a
    elif (b> c) and (b > a):
        return b
    else:
        return c
