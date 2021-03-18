def count_vowels(sentence):
    """
    Return the number of vowels (a,e,i,o,u) in a sentence.
    >>> count_vowels("Hello World!")
    3
    >>> count_vowels("baa baa do baa baa")
    9
    >>> count_vowels("HELLO")
    2
    >>> count_vowels("zzz")
    0
    """
    
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0

    for c in sentence:
        if(c.lower() in vowels):
            vowel_count += 1
    return vowel_count

def count_upper(sentence):
    """
    >>> count_upper("Hello World!")
    2
    >>> count_upper("27th of April 1968")
    1
    >>> count_upper("HELLO")
    5
    >>> count_upper("zzz")
    0
    """
    upper = 0
    for c in sentence:
        if(c.isupper()):
            upper += 1

    return upper

def match_brackets(s):
    '''
    >>> match_brackets('(7 - 4) * (3 + 2)')
    True
    >>> match_brackets('((2 + 5) / (13 +12)')
    False
    >>> match_brackets(')14 + 12) % 3')
    False
    >>> match_brackets(')(')
    False
    >>> match_brackets('())(')
    False
    >>> match_brackets('())(()()')
    False
    >>> match_brackets('())()(')
    False
    '''
    open = 0
    for c in s:
        if(open < 0):
            return False

        if(c == "("):
            open += 1
        elif(c == ")"):
            open -= 1
    
    if(open == 0):
        return True
    else:
        return False

def get_ords(s):
    '''
    >>> get_ords('abc')
    '97 98 99 '
    >>> get_ords('a b c')
    '97 32 98 32 99 '
    >>> get_ords('a1 b2 c3')
    '97 49 32 98 50 32 99 51 '
    >>> get_ords('[(!)]')
    '91 40 33 41 93 '
    '''
    ordstr = ""
    for c in s:
        ordstr += str(ord(c)) + " "
    
    return ordstr

def ballon_string(string, x):
    '''
    >>> balloon_string('abcdef', 4)
    'abbccceff'
    >>> balloon_string('A great day!', 4)
    'Agggrreaay!'
    >>> balloon_string('ABC 1234', 3)
    'AAC 1224'
    '''
    output = ""
    for c in string:
        output += (ord(c) % x) * c

    return output

print(count_vowels("Hello World"))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)