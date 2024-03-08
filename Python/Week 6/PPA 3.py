"""
Write the following functions:

(1) is_key: accept a dictionary D and a variable key as arguments. Return True if the variable key is a key of the dictionary D, and False otherwise.

(2) value: accept a dictionary D and a variable key as arguments. If the variable key is not a key of the dictionary D, return None, otherwise, return the value corresponding to this key.

You do not have to accept input from the user or print the output to the console. You just have to write the definition of both the functions.

"""


def is_key(D, key):
    if key in D.keys():
        return True
    else:
        return False
        
def value(D, key)
    if is_key(D, key):
        return D[key]
    else:
        return None
