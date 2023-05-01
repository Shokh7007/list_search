def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=0
    b=0
    while a<len(data):
        if data[a]>b:
            b=data[a]
        a+=1
    d=data.count(b)
    return d
print(find_max_count([1, 8, 3, 8, 5]))
