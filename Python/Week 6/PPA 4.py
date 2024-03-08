"""
Write a function named value_to_keys that accepts a dictionary D and a variable named value as arguments.
It should return the list of all keys in the dictionary that have value equal to value. 
If the value is not present in the dictionary, the function should return the empty list.

(1) You do not have to accept input from the user or print the output to the console. You just have to write the definition of the function.

(2) The keys inside the list could be in any order.


"""
def value_to_keys(D, value):
    keys =[]
    for k, v in D.items(): 
        if v == value:
            keys.append(k)
    return keys

