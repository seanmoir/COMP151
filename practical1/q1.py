def is_dope(number):
    """   
    >>> is_dope(123)
    True
    >>> is_dope(321)
    True
    >>> is_dope(22)
    True
    >>> is_dope(232)
    False
    >>> is_dope(10)
    False
    """
    out_mult = 1
    out_add = 0    
    for c in str(number):
        out_mult *= int(c)
        out_add += int(c)

    if(out_add == out_mult):
        return True
    else:
        return False




def convert_phone(number):
    """
    >>> convert_phone(22)
    'cc'
    >>> convert_phone(1403)
    'bead'
    >>> convert_phone(345901)
    'defjab'
    """
    out = ""
    for c in str(number):
        out += chr(int(c) + 97)
    
    return out



if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)