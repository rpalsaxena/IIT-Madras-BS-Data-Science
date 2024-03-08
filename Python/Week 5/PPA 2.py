def check_leap_year(year):
    """
    check if the year is a leap year or not

    Argument:
        year: integer
    Return:
        is_leap_year: bool
    """
    if year%100 == 0:
        return True
    elif year%4 == 0:
        return True
    else:
        return False
