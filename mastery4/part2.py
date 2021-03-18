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

print(count_vowels("Hello World"))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)