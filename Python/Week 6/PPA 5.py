"""
Write the following functions:

(1) dict_to_list: accept a dictionary D as argument. Return the key-value pairs in D as a list L of tuples. That is, every element of L should be of the form (key, value) such that D[key] = value. Going the other way, every key-value pair in the dictionary should be present as a tuple in the list L.

(2) list_to_dict: accept a list of tuples L as argument. Each element of L is of the form (x, y). Return a dict D such that each tuple (x, y) corresponds to a key-value pair in D. That is, D[x] = y.

(1) For the function dict_to_list(D), the order in which the key-value pairs are appended to the list doesn't matter.

(2) For the function list_to_dict(L), you can assume that if (x1, y1) and (x2, y2) are two different elements in L, x1 != x2. Why is this assumption important?

(3) You do not have to accept input from the user or print the output to the console. You just have to write the definition of both the functions.


"""
def dict_to_list(D):
    items = []
    for k,v in D.items():
        items.append((k,v))
    return items

def list_to_dict(L):
    D ={}
    for i in L:
        D[i[0]] = i[1]
    return D
