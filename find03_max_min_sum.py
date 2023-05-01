def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    a=0
    b=data[0]
    while a<len(data):
        if data[a]<b:
            b=data[a]
        a+=1
    c=0
    d=0
    while c<len(data):
        if data[c]>d:
            d=data[c]
        c+=1
    return b+d
print(find_max_min_sum([1, 2, 3, 4, 5]))