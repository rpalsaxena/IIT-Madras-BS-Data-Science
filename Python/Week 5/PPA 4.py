def first_three(L):
    '''
    find the first three maximums in the list
    Argument:
        L: list of ints
    Return:
        (fmax, smax, tmax): (int, int, int)
    '''
    if len(L) < 3:
        return False
        
    fmax = max(L)
    L.remove(fmax)
    
    smax = max(L)
    L.remove(smax)

    tmax = max(L)
    
    #print(fmax)
    return (fmax, smax, tmax)
