def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    # s_list = []
    # r_list = []
    # vowels = []

    # for char in s:  #create an array of characters replacing vowels with 'vowel' 
    #     if char in 'aeiouAEIOU':
    #         s_list.append('vowel')
    #         vowels.append(char)  #and creating a list of vowels to reverse
    #     else:
    #         s_list.append(char)
    
    # for char in s_list:   #rebuilding a reversed list 
    #     if char == 'vowel':
    #         r_list.append(vowels.pop())  #and adding reversed vowels
    #     else:
    #         r_list.append(char)

    # return ''.join(r_list)

    # vowels = set('aeiouAEIOU')

    # s_list = list(s)
    # i = 0
    # j = len(s) - 1

    # while i < j:
    #     if s_list[i] in vowels and s_list[j] in vowels:
    #         [s_list[i], s_list[j]] = [s_list[j], s_list[i]]
    #         i += 1
    #         j -= 1
    #     elif s_list[i] in vowels:
    #         j -= 1
    #     elif s_list[j] in vowels:
    #         i += 1
    #     else:
    #         i += 1
    #         j -= 1
    
    # return ''.join(s_list)

###############################


    vowels = set('aeiouAEIOU')

    s_list = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if s_list[i] not in vowels:
            i += 1
        if s_list[j] not in vowels:
            j -= 1
        else:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
    
    return ''.join(s_list)


