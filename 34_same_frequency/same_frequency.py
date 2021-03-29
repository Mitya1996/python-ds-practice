def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # set1 = set(list(str(num1)))
    # set2 = set(list(str(num2)))

    # return set1 == set2
    ###########

    frequency = {}

    for num in str(num1):
        frequency[num] = frequency.get(num, 0) + 1

    for num in str(num2):
        frequency[num] = frequency.get(num, 0) - 1

    return sum(frequency.values()) == 0