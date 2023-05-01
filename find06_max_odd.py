def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a=0
    b=0
    while a<len(data):
        if data[a]%2==1:
            if data[a]>b:
                b=data[a]
        a+=1
    return b
print(find_max_odd([7, 6, 10, 3, 4, 9]))