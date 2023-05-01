def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    a=0
    b=0
    while a<len(data):
        if data[a]>b:
            b=data[a]
        a+=1
    return b
print(find_max([1, 2, 3, 4, 5]))
    