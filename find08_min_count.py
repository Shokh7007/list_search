def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    a=0
    b=data[0]
    while a<len(data):
        if data[a]<b:
            b=data[a]
        a+=1
    d=data.count(b)
    return d
print(find_min_count([9, 8, 3, 8,3, 5]))
