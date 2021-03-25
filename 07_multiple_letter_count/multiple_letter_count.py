def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count_dict = {}
    
    for char in phrase:
        count_dict[char] = count_dict.get(char, 0) + 1

    return count_dict #refactored from a longer way