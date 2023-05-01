def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    a=0
    b=data[0]
    while a<len(data):
        if data[a]<b:
            b=data[a]
        a+=1
    c=data.index(b)
    return c
print(find_min_index([10, 2, 8, 4, 5]))

