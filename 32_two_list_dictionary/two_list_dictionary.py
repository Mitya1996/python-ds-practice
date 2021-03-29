def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    # vals_copy = values #to not mutate original
    # if len(values) > len(keys):
    #     vals_copy = values[:len(keys)] #truncate values list if too long
    
    # if len(values) < len(keys):
    #     for i in range(len(keys) - len(values)):
    #         vals_copy.append(None)  #append none for however many values are missing
        
    # dct = {}

    # count = 0    
    # while count < len(keys):
    #     dct[keys[count]] = vals_copy[count]
    #     count += 1
    
    # return dct
##############################
    # dct = {}

    # for idx, key in enumerate(keys):
    #     if idx < len(values):
    #         dct[key] = values[idx]
    #     else:
    #         dct[key] = None

    # return dct
##################################
    # dct = {}

    # for idx, key in enumerate(keys):
    #     dct[key] = values[idx] if idx < len(values) else None

    # return dct
##################################

    return {key:(values[idx] if idx < len(values) else None) for (idx, key) in enumerate(keys)}

################################
    # from itertools import zip_longest

    # return dict(zip_longest(keys,values)) #this creates 'None' keys if values list is longer ...