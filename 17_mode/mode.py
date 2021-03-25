def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dct = {}
    for num in nums:
        dct[num] = dct.get(num, 0) + 1
    
    #get index of max in values
    max_val = max(dct.values()) 
    # index = list(dct.values()).index(max_val)

    # return list(dct.keys())[index] #return keys[index]

    #with python it's easier to get the index of a dictionary
    #you can unpack and you have pairs "items"
    for (key,val) in dct.items():
        if val == max_val:
            return key