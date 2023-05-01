def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    a=0
    b=0
    while a<len(data):
        if data[a]%2==0:
            if data[a]>b:
                b=data[a]
        a+=1
    return b
print(find_max_even([7, 6, 3, 4, 9]))
