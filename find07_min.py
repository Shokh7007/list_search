def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    a=0
    b=data[0]
    while a<len(data):
        if data[a]<b:
            b=data[a]
        a+=1
    return b
print(find_min([1, 2, 3, 4, 5]))