def factorial(n):
    """
    computes the factorial of an integer
    
    Argument:
        n: integer
    Return:
        result: integer
    """
    if n <0:
        return -1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
