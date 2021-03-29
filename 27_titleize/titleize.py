def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # split = phrase.lower().rsplit(' ')
    # return ''.join([word.capitalize() for word in split])
    return phrase.title()