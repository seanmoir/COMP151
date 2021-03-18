def find_slice(s, ch):
    """
    >>> find_slice("abcdefghijk", "f")
    'abcdef'
    >>> find_slice("aaabbbccc", "b")
    'aaab'
    >>> find_slice("aaabbbccc", "d")
    ''
    """
    pos = s.find(ch)
    if(pos == 0):
        return ""
    else:
        return s[:pos + 1]

def first_half(s):
    '''
    >>> first_half("abcdef")
    'abc'
    >>> first_half("abcdefg")
    'abc'
    >>> first_half("a")
    ''
    >>> first_half("good dogs")
    'good'
    '''
    return s[:len(s) // 2]

def second_half(s):
    '''
    >>> second_half("abcdef")
    'def'
    >>> second_half("abcdefg")
    'efg'
    >>> second_half("a")
    ''
    >>> second_half("good dogs")
    'dogs'
    '''
    if(len(s) % 2 == 0):
        return s[len(s) // 2:]
    else:
        return s[(len(s) // 2 + 1):]

def extension_remover(file_name):
    '''
    >>> extension_remover("my_text_file.txt")
    'my_text_file'
    >>> extension_remover("data.2015.docx")
    'data.2015'
    '''
    pos = file_name.rfind(".")
    return file_name[:pos]

def multi_blank(s, n):
    '''
    >>> multi_blank("banana", 1)
    'b*****'
    >>> multi_blank("bread", 1)
    'b****'
    >>> multi_blank("banana", 2)
    'ba****'
    >>> multi_blank("banana", 3)
    'ban***'
    >>> multi_blank("chips", 0)
    '*****'
    '''
    return s[:n] + ((len(s) - n) * "*")

word = input()
print(find_slice(word, "h"))
print(first_half(word))
print(second_half(word))
print(extension_remover("my_text.file.txt"))
print(multi_blank("bannana", 1))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)