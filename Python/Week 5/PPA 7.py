def is_empty(L):
    '''
    check if the list is empty
    Argument:
        L: list
    Return:
        result: boolean
    '''
    if len(L) ==0:
        return True
    else:
        return False
    

def first(L):
    '''
    return the first element of the list
    Argument:
        L: list
    Return:
        result: int
    '''
    if not is_empty(L):
        return L[0]
    else:
        return None
        
def last(L):
    '''
    return the last element of the list
    Argument:
        L: list
    Return:
        result: int
    '''
    
    if not is_empty(L):
        return L[-1]
    else:
        return None
        

def init(L):
    '''
    return first n - 1 elements of the list
    Argument:
        L: list
    Return:
        result: list
    '''
    if not is_empty(L):
        return L[:-1]
    else:
        return None


def rest(L):
    '''
    return the last n - 1 elements of the list
    Argument:
        L: list
    Return:
        result: list
    '''
    if not is_empty(L):
        return L[1:]
    else:
        return None

